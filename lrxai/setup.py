from setuptools import setup, find_packages

setup(
    name='lrxai',  
    version='0.1.0',                
    packages=find_packages(),       
    description='A simple custom logistic regression library',  
    #long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    author='Yilmaz Unal',             
    author_email='yilmazunal16@egmail.com', 
    keywords=['logistic regression', 'machine learning'],  
    install_requires=[
        'numpy',  
        
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',  
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',  
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
