from setuptools import find_packages, setup

setup(
    name='netbox-journal-calendar',
    version='1.2.1',
    description='Calendario interattivo per Journal Entries con filtri avanzati',
    long_description='Visualizza la cronologia degli interventi su una griglia temporale mensile filtrabile per Sito, Device e Tags.',
    url='https://github.com/stefanoparis-mgh/netbox-journal-calendar',
    author='Stefano Paris',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
