from setuptools import setup

setup(
        name="minGPT",
        version="0.0.1",
        author="Andrej Karpathy",
        author_email="andrej.karpathy@gmail.com",
        packages=["minGPT"],
        url="https://github.com/karpathy/minGPT",
        license="MIT",
        install_requires=[
                "numpy >= 1.8",
                "torch >= 1.9"
        ]
)
