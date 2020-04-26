# Lambda Zip (lamzip)
#
# Description: A lightweight utility for packaging a Python source directory
#   to be used as an AWS Lambda function.  This utility is not intended to
#   deploy the zip package to a function.  This utility is useful for
#   incremental pipelines where another process might be used for package
#   upload, or manual action is required.
# Author: Sean Sydow
# Version: 0.4.1
#

import os
import yaml
import click
import zipfile


# used for deploying an example config_file
config_example = """
# Lambda-Zip (lamzip)
#
# Defaults for packaging your AWS Lambda function
#

source-directory: ./appsrc
destination-directory: ./dist
package-prefix: foo
package-version: 0.0.1
"""


# return dict object from yaml config_file
def load_defaults(config_file):

    with open(config_file) as cf:
        _defaults = yaml.safe_load(cf)
        return _defaults


# zip a source directory contents - do not include folder itself in zip
# ./my_src_dir/dir/file1 -> ./dir/file1
def zip_dir_contents(src_dir, dest_dir, zip_prefix, zip_version):

    # basic checks
    if not os.path.exists(src_dir):
        print(f"Source directory does not exist, exiting")
        exit(1)
    if not os.path.exists(dest_dir):
        print(f"Destination directory does not exist, exiting")
        exit(1)

    # create zipped package
    zip_filename = f"{zip_prefix}-{zip_version}.zip"
    zip_path = os.path.join(dest_dir, zip_filename)
    print(f"Creating Archive: {zip_path}")
    zf = zipfile.ZipFile(zip_path, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=5)

    try:
        for (dir_path, dir_names, file_names) in os.walk(src_dir):
            for file in file_names:
                rel_file_path = os.path.join(dir_path, file)
                alt_file_path = os.path.join(dir_path.replace(src_dir, ''), file)
                print(f'  adding: {rel_file_path}')
                zf.write(rel_file_path, arcname=alt_file_path)
    finally:
        zf.close()


# for pre-defined settings in configuration file (click)
@click.group()
def main():
    pass


# for click command "make-config" (create example yaml config file)
@main.command('make-config')
@click.option('-n', '--config-name', help='Create an example config file (using specified name)')
def make_config(config_name):

    _config_name = '.lamzip.yaml'
    if config_name:
        _config_name = config_name

    click.echo(f"LamZip writing example config file: {_config_name}")

    # write example config_file to local directory
    with open(_config_name, 'w') as c:
        c.write(config_example)


# for click command "use-config" (get settings from yaml config file)
@main.command('use-config')
@click.option('-c', '--config-file',
              default='.lamzip.yaml',
              type=click.Path(),
              show_default=True,
              help='Config file')
def use_config(config_file):

    click.echo(f"LamZip using existing config file: {config_file}")

    defaults = {}
    # use defaults configuration file, if found
    if os.path.exists(config_file):
        defaults = load_defaults(config_file)
        click.echo(f"  Source Dir: {defaults.get('source-directory')}")
        click.echo(f"  Destination Dir: {defaults.get('destination-directory')}")
        click.echo(f"  Package Prefix: {defaults.get('package-prefix')}")
        click.echo(f"  Package Version: {defaults.get('package-version')}")
        click.echo()
        zip_dir_contents(
            str(defaults.get('source-directory')),
            str(defaults.get('destination-directory')),
            str(defaults.get('package-prefix')),
            str(defaults.get('package-version')))
    else:
        click.echo(f"Config file not found: {config_file}")


# for click command "specify" (manually specify settings on cli)
@main.command('specify')
@click.option('-s', '--src-dir',
              required=True,
              help='Source directory (containing code)')
@click.option('-d', '--dest-dir',
              required=True,
              default='./dist',
              show_default=True,
              help='Destination directory (zip)')
@click.option('-p', '--zip-prefix',
              required=True,
              help='Distribution package name (version appended)')
@click.option('-v', '--zip-version',
              required=True,
              help='Distribution package version (Ex: 0.1.3)')
def specify(src_dir, dest_dir, zip_prefix, zip_version):

    click.echo(f"LamZip using CLI specification:")
    click.echo(f"  Source Dir: {src_dir}")
    click.echo(f"  Destination Dir: {dest_dir}")
    click.echo(f"  Package Prefix: {zip_prefix}")
    click.echo(f"  Package Version: {zip_version}")
    click.echo()

    zip_dir_contents(
        src_dir=src_dir,
        dest_dir=dest_dir,
        zip_prefix=zip_prefix,
        zip_version=zip_version)


if __name__ == "__main__":

    main()
