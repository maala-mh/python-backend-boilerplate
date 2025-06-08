from setuptools import find_packages, setup

setup(
    name='htmltopdfapp',
    version='1.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    entry_points={
    },
    scripts=[],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11',
    ],
)
