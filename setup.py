from setuptools import find_packages, setup

setup(
	name='PokemonGame',
	version='0.0.0',
	packages=find_packages(),
	include_package_data= True,
	zip_safe= False,
	install_requires=[
		'pygame',
        'pytmx',
	],
	extras_require={

	}
)
