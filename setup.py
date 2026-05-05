
from setuptools import find_packages, setup
from distutils.command.build import build
import os

class BuildMessages(build):
    def run(self):
        try:
            from django.core.management import call_command
            call_command('compilemessages')
        except ImportError:
            print("Django not found. Skip compiling messages")
        build.run(self)


setup(
    name='netbox-journal-calendar',
    version='2.5.8',
    description='Interactive Calendar for Journal Entries',
    long_description='Display journal entry as a calendar view',
    url='https://github.com/stefanoparis-mgh/netbox-journal-calendar',
    author='Stefano Paris',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='Apache 2.0',
    cmdclass={
        'build_messages': BuildMessages,
    },
)
