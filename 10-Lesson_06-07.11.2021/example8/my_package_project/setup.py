# setuptool modülü için script oluşturur.
# setupçpy dynamic bir yapıdadır. setap yaplırken kod blokları çalıştırılabilir
# birde setup.cfg var bu da statik bir yapı sunar. statik bilgiler içindir. 
# mesela alttaki birçok bilgi aslında bu static setup.cfg dosyasında tutulabilir.

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Murat Çabuk",
    author_email="mcabuk@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muratcabuk/sample_python_package",
    project_urls={
        "Bug Tracker": "https://github.com/muratcabuk/sample_python_package/issues",
    },
    # python pypi da gecen kategoriler
    # https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "my_package"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
    entry_points={
        'console_scripts': [
            'my_package = my_package.main_pkg.main_module:main_fonksiyon',
        ],    },
)