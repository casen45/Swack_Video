from setuptools import find_packages, setup

setup(name="swack-multimedia",
      version="0.1.0",
      keywords=["multimedia"],
      description="Multimedia files processing.",
      license="GNU",
      author="Casen",
      author_email="casen@swack.win",
      packages=find_packages(),
      install_requires=["numpy>=1.16.0", "opencv-python>=4.0.0"],
      platforms="any",
      url="https://github.com/casen45/swack-multimedia",
      zip_safe=False,
      )
