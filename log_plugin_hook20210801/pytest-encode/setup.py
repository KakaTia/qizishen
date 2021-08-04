from setuptools import setup

setup(
    # name是要安装的包名，就是pip install XX
    name='pytest_encode',
    # 包的github链接
    url='https://github.com/KakaTia/qizishen/pytest-encode',
    version='1.0',
    author="qizishen",
    author_email='89717045@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[  # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['pytest_encode'],
    # 别人搜索时常用的关键字
    keywords=[
        'pytest', 'py.test', 'pytest_encode',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 最关键的步骤：入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest_encode = pytest_encode',
        ]
    },
    # windows系统需要的，mac不用写这段
    zip_safe=False
)
