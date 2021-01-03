{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "NgUeapcvmIRh"
   },
   "source": [
    "# **Assignment For Numpy**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yhr3JicwnA-4"
   },
   "source": [
    "Difficulty Level **Beginner**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hVPqDJ1SnKSh"
   },
   "source": [
    "1. Import the numpy package under the name np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "SePu31zKmgS-"
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "d0gO81krnL7g"
   },
   "source": [
    "2. Create a null vector of size 10 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "2s6o2JPgnSBr"
   },
   "outputs": [],
   "source": [
    "arr = np.zeros((10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BJTMK03fnS1w"
   },
   "source": [
    "3. Create a vector with values ranging from 10 to 49"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "qRXxXuWdnj1M"
   },
   "outputs": [],
   "source": [
    "rng = np.arange(10,49)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "n63lzg5Onkcn"
   },
   "source": [
    "4. Find the shape of previous array in question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "1FueBdqPn_q7"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(39,)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rng.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "AzMlQj1MoAVe"
   },
   "source": [
    "5. Print the type of the previous array in question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "AO9PYmdWoE1L"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rng.dtype"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0qaKS13Yon-U"
   },
   "source": [
    "6. Print the numpy version and the configuration\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "T3wY24e1oorh"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.18.1\n",
      "blas_mkl_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/ProgramData/Anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/ProgramData/Anaconda3\\\\Library\\\\include']\n",
      "blas_opt_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/ProgramData/Anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/ProgramData/Anaconda3\\\\Library\\\\include']\n",
      "lapack_mkl_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/ProgramData/Anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/ProgramData/Anaconda3\\\\Library\\\\include']\n",
      "lapack_opt_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/ProgramData/Anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/ProgramData/Anaconda3\\\\Library\\\\include']\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(np.__version__)\n",
    "print(np.show_config())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZyUUiQf5oyvE"
   },
   "source": [
    "7. Print the dimension of the array in question 3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "pLXfuIqIo0vq"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(rng.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JYVMuFrqpBdV"
   },
   "source": [
    "8. Create a boolean array with all the True values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "3apZsISzpFKR"
   },
   "outputs": [],
   "source": [
    "boolean = np.ones((10),dtype=bool)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "4zbBooWZpPBU"
   },
   "source": [
    "9. Create a two dimensional array\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "KfPQEiVIpdTo"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "twoDim = np.zeros((10,10))\n",
    "print(twoDim.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "do9wPAFbpqC7"
   },
   "source": [
    "10. Create a three dimensional array\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "ZCO_q-KZqAeW"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "threedim = np.zeros((10,10,10))\n",
    "print(threedim.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a4iysJ87qEeb"
   },
   "source": [
    "Difficulty Level **Easy**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DehgqszSqjY6"
   },
   "source": [
    "11. Reverse a vector (first element becomes last)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "tfevmc4VqkWu"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-0.46954462 -1.11476422 -0.34774951  1.42072827 -0.17227768 -0.85706922\n",
      "  0.44668853  0.87560176 -0.44015905 -0.22783064]\n",
      "[-0.22783064 -0.44015905  0.87560176  0.44668853 -0.85706922 -0.17227768\n",
      "  1.42072827 -0.34774951 -1.11476422 -0.46954462]\n"
     ]
    }
   ],
   "source": [
    "reverse = np.random.randn((10))\n",
    "print(reverse)\n",
    "reverse = np.flip(reverse)\n",
    "print(reverse)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yoATXS-qqk_q"
   },
   "source": [
    "12. Create a null vector of size 10 but the fifth value which is 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "AheZ32Owqpte"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 0 0 1 0 0 0 0 0]\n"
     ]
    }
   ],
   "source": [
    "nullVector = np.array([1 if x == 4 else 0 for x in range(10)])\n",
    "print(nullVector)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "RZRzOBbFsY0w"
   },
   "source": [
    "13. Create a 3x3 identity matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "va2ou0BHsvEj"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "identity = np.identity(3)\n",
    "print(identity)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "lnN5drkUs6o2"
   },
   "source": [
    "14. arr = np.array([1, 2, 3, 4, 5]) \n",
    "\n",
    "---\n",
    "\n",
    " Convert the data type of the given array from int to float "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "59EIQt6otKUB"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr = np.array([1,2,3,4,5],dtype=float)\n",
    "arr.dtype"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fSL2AKJetTes"
   },
   "source": [
    "15. arr1 =          np.array([[1., 2., 3.],\n",
    "\n",
    "                    [4., 5., 6.]])  \n",
    "                      \n",
    "    arr2 = np.array([[0., 4., 1.],\n",
    "     \n",
    "                   [7., 2., 12.]])\n",
    "\n",
    "---\n",
    "\n",
    "\n",
    "Multiply arr1 with arr2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "7VDXgRQDuJNV"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.,  8.,  3.],\n",
       "       [28., 10., 72.]])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])  \n",
    "arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])\n",
    "arr1 * arr2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a8yJ438-uKni"
   },
   "source": [
    "16. arr1 = np.array([[1., 2., 3.],\n",
    "                    [4., 5., 6.]]) \n",
    "                    \n",
    "    arr2 = np.array([[0., 4., 1.], \n",
    "                    [7., 2., 12.]])\n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "Make an array by comparing both the arrays provided above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "3MPDaAlYueF3"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[False False False]\n",
      " [False False False]]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.array([[1., 2., 3.],[4., 5., 6.]]) \n",
    "arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])\n",
    "arr3 = arr1 == arr2\n",
    "print(arr3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "3xiD0eJluewk"
   },
   "source": [
    "17. Extract all odd numbers from arr with values(0-9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "id": "J_qbt_EuvM7l"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 3 5 7 9]\n"
     ]
    }
   ],
   "source": [
    "odd = np.arange(0,10)\n",
    "print(odd[odd % 2 != 0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "zpg5cyLsvPoZ"
   },
   "source": [
    "18. Replace all odd numbers to -1 from previous array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "id": "rXUV1-ULvQdd"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0 -1  2 -1  4 -1  6 -1  8 -1]\n"
     ]
    }
   ],
   "source": [
    "odd[odd % 2 != 0] = -1\n",
    "print(odd)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "FWpHTWTDvjvi"
   },
   "source": [
    "19. arr = np.arange(10)\n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "Replace the values of indexes 5,6,7 and 8 to **12**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "ensZ3lqwvlSb"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  1  2  3  4 12 12 12 12  9]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange(10)\n",
    "arr[[5,6,7,8]] = 12\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ib-vBffAv0zy"
   },
   "source": [
    "20. Create a 2d array with 1 on the border and 0 inside"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "id": "RmzcjNYrwDrM"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1. 1. 1.]\n",
      " [1. 0. 0. 1.]\n",
      " [1. 0. 0. 1.]\n",
      " [1. 1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "twoD = np.ones((4,4))\n",
    "twoD[1:-1,1:-1] = 0\n",
    "print(twoD)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "E1diIFSEwEmh"
   },
   "source": [
    "Difficulty Level **Medium**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eGLZmNb_wKb4"
   },
   "source": [
    "21. arr2d = np.array([[1, 2, 3],\n",
    "\n",
    "                    [4, 5, 6], \n",
    "\n",
    "                    [7, 8, 9]])\n",
    "\n",
    "---\n",
    "\n",
    "Replace the value 5 to 12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "id": "VdUnsUOZwJFz"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3]\n",
      " [ 4 12  6]\n",
      " [ 7  8  9]]\n"
     ]
    }
   ],
   "source": [
    "arr2d = np.array([[1, 2, 3],\n",
    "                  [4, 5, 6], \n",
    "                  [7, 8, 9]])\n",
    "arr2d = np.where(arr2d == 5,12,arr2d)\n",
    "print(arr2d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "TEbFhlPZxaKO"
   },
   "source": [
    "22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])\n",
    "\n",
    "---\n",
    "Convert all the values of 1st array to 64\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "id": "eYzephU8xmsg"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[64 64 64]\n",
      "  [ 4  5  6]]\n",
      "\n",
      " [[ 7  8  9]\n",
      "  [10 11 12]]]\n"
     ]
    }
   ],
   "source": [
    "arr3d = np.array([\n",
    "    [\n",
    "        [1, 2, 3], \n",
    "        [4, 5, 6]\n",
    "    ], \n",
    "    [\n",
    "        [7, 8, 9], \n",
    "        [10, 11, 12]\n",
    "    ]\n",
    "])\n",
    "arr3d[0][0] = 64\n",
    "print(arr3d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vZj0Ndvnx6f0"
   },
   "source": [
    "23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "id": "pM4e9YfdyHSv"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2 3 4]\n",
      " [5 6 7 8 9]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2d = np.arange(0,10).reshape((2,5))\n",
    "print(arr2d)\n",
    "arr2d[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "C3dkW0lZyVps"
   },
   "source": [
    "24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "id": "IrrzK2xgygqV"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2 3 4]\n",
      " [5 6 7 8 9]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2d = np.arange(0,10).reshape((2,5))\n",
    "print(arr2d)\n",
    "arr2d[1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "G3dLwOO9yyrE"
   },
   "source": [
    "25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "id": "5Bx4fqsLyqGD"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2 3 4]\n",
      " [5 6 7 8 9]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([2, 7])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2d = np.arange(0,10).reshape((2,5))\n",
    "print(arr2d)\n",
    "arr2d[:,2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "CQ9YST5jy0IL"
   },
   "source": [
    "26. Create a 10x10 array with random values and find the minimum and maximum values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "id": "lhJPugjQzG6W"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimun Value -2.2837477221381985\n",
      "Maximum Value 2.5620789179742998\n"
     ]
    }
   ],
   "source": [
    "rand = np.random.randn((100)).reshape((10,10))\n",
    "print(f\"Minimun Value {np.amin(rand)}\")\n",
    "print(f\"Maximum Value {np.amax(rand)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cAgDt6KazHk6"
   },
   "source": [
    "27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "---\n",
    "Find the common items between a and b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "id": "kBXZanxIzs_F"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Common Elements are : [2 4]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,2,3,2,3,4,3,4,5,6]) \n",
    "b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "print(f\"Common Elements are : {np.intersect1d(a,b)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "lF9IzWOAztpD"
   },
   "source": [
    "28. a = np.array([1,2,3,2,3,4,3,4,5,6])\n",
    "b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "\n",
    "---\n",
    "Find the positions where elements of a and b match\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "id": "JR-mHQLH0HY_"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 5], dtype=int64)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.searchsorted(a, np.intersect1d(a, b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "mMDiefpH0H1x"
   },
   "source": [
    "29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)\n",
    "\n",
    "---\n",
    "Find all the values from array **data** where the values from array **names** are not equal to **Will**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "id": "gfc1Lpf81ZSR"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.79529215 -0.97741749 -0.0115015   0.62815036]\n",
      " [ 1.47258734  0.64927411  0.38251237 -0.1831414 ]\n",
      " [-0.59991043 -2.07044163 -1.97703271  0.4341415 ]\n",
      " [ 2.57267336  0.13793104 -0.0630175  -1.27429978]\n",
      " [-0.49516058  0.16005144  0.1652926   1.12793848]\n",
      " [-0.4754079  -1.39395656 -1.16842394  0.25117908]\n",
      " [-0.52900326  0.37646031  1.58657871 -1.8663994 ]]\n",
      "==================================================\n",
      "[[ 0.79529215 -0.97741749 -0.0115015   0.62815036]\n",
      " [ 1.47258734  0.64927411  0.38251237 -0.1831414 ]\n",
      " [ 2.57267336  0.13793104 -0.0630175  -1.27429978]\n",
      " [-0.4754079  -1.39395656 -1.16842394  0.25117908]\n",
      " [-0.52900326  0.37646031  1.58657871 -1.8663994 ]]\n"
     ]
    }
   ],
   "source": [
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) \n",
    "data = np.random.randn(7, 4)\n",
    "print(data)\n",
    "print('==================================================')\n",
    "print(data[names != 'Will'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "52zEjDMf1aXS"
   },
   "source": [
    "30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)\n",
    "\n",
    "---\n",
    "Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "id": "8RYG0kLO1mHw"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.79529215 -0.97741749 -0.0115015   0.62815036]\n",
      " [ 1.47258734  0.64927411  0.38251237 -0.1831414 ]\n",
      " [-0.59991043 -2.07044163 -1.97703271  0.4341415 ]\n",
      " [ 2.57267336  0.13793104 -0.0630175  -1.27429978]\n",
      " [-0.49516058  0.16005144  0.1652926   1.12793848]\n",
      " [-0.4754079  -1.39395656 -1.16842394  0.25117908]\n",
      " [-0.52900326  0.37646031  1.58657871 -1.8663994 ]]\n",
      "==================================================\n",
      "[[ 0.79529215 -0.97741749 -0.0115015   0.62815036]\n",
      " [ 2.57267336  0.13793104 -0.0630175  -1.27429978]]\n"
     ]
    }
   ],
   "source": [
    "print(data)\n",
    "print('==================================================')\n",
    "mask = (names != 'Will') & (names!= 'Joe')\n",
    "print(data[mask])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Q7hjf2bd2dCY"
   },
   "source": [
    "Difficulty Level **Hard**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b48g7aRA2jVM"
   },
   "source": [
    "31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "id": "EbwfSCrW2f9_"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 7.81446439 10.43375573 10.16551344]\n",
      " [ 7.62760006  4.34657656  9.78630061]\n",
      " [ 2.65405128  1.93917704  5.15795405]\n",
      " [ 1.30546528  1.22005902 10.89347907]\n",
      " [ 6.2359925  14.52031755  3.10523591]]\n"
     ]
    }
   ],
   "source": [
    "rand_arr = np.random.uniform(1,15, size=(5,3))\n",
    "print(rand_arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ei_nDHtO3qBk"
   },
   "source": [
    "32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "id": "phOxVpBM4M6D"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[15.15473342  7.0006862   6.73750864  3.20200098]\n",
      "  [ 6.91905867  2.75517021 10.44271079  7.32215179]]\n",
      "\n",
      " [[ 1.31953923 11.49166214 15.00252242 12.36304854]\n",
      "  [ 5.01844487 12.6056016  10.87239401 15.91025734]]]\n"
     ]
    }
   ],
   "source": [
    "rand_arr2 = np.random.uniform(1,16, size=(2,2,4))\n",
    "print(rand_arr2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "uyiQaMjA4d_x"
   },
   "source": [
    "33. Swap axes of the array you created in Question 32"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "id": "w2m9p8064VtR"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array\n",
      "[[[15.15473342  7.0006862   6.73750864  3.20200098]\n",
      "  [ 6.91905867  2.75517021 10.44271079  7.32215179]]\n",
      "\n",
      " [[ 1.31953923 11.49166214 15.00252242 12.36304854]\n",
      "  [ 5.01844487 12.6056016  10.87239401 15.91025734]]]\n",
      "Swapped Axes\n",
      "[[[15.15473342  1.31953923]\n",
      "  [ 6.91905867  5.01844487]]\n",
      "\n",
      " [[ 7.0006862  11.49166214]\n",
      "  [ 2.75517021 12.6056016 ]]\n",
      "\n",
      " [[ 6.73750864 15.00252242]\n",
      "  [10.44271079 10.87239401]]\n",
      "\n",
      " [[ 3.20200098 12.36304854]\n",
      "  [ 7.32215179 15.91025734]]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Original Array\")\n",
    "print(rand_arr2)\n",
    "print(\"Swapped Axes\")\n",
    "print(np.swapaxes(rand_arr2, 2, 0))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "2dlU_yUR4mVZ"
   },
   "source": [
    "34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "id": "tmBabEJ-5JgB"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 3 4 2 2 2 2 3 1 2]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.uniform(0,20, size=(10))\n",
    "arr = arr.astype('int32') \n",
    "arr =np.sqrt(arr)\n",
    "arr = np.where(arr < 0.5, 0, arr)\n",
    "arr = arr.astype('int32')\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SNAM4dpu5RKA"
   },
   "source": [
    "35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "id": "3pxebU2b5q9Z"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 1 : [ 2.60253676  7.30885072 18.01068431  8.59087495 13.64285454 17.42513991\n",
      "  8.04970923 13.55299142 13.69942044  4.64221238]\n",
      "Array 2 : [ 9.5375168   4.53542701  1.99919546  7.36975435 19.54735766  3.25443618\n",
      "  4.78978505 13.30194616  5.90724213  5.67375285]\n",
      "New Array : [ 9.5375168   7.30885072 18.01068431  8.59087495 19.54735766 17.42513991\n",
      "  8.04970923 13.55299142 13.69942044  5.67375285]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.uniform(0,20, size=(10))\n",
    "arr1 = np.random.uniform(0,20, size=(10))\n",
    "newArr = np.maximum(arr,arr1)\n",
    "print(f\"Array 1 : {arr}\")\n",
    "print(f\"Array 2 : {arr1}\")\n",
    "print(f\"New Array : {newArr}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fz_bpqm28qmD"
   },
   "source": [
    "36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])\n",
    "\n",
    "---\n",
    "Find the unique names and sort them out!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "id": "hiSNMgcY87Ey"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Bob' 'Joe' 'Will']\n"
     ]
    }
   ],
   "source": [
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])\n",
    "print(np.sort(np.unique(names)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dguMNzob870H"
   },
   "source": [
    "37. a = np.array([1,2,3,4,5])\n",
    "b = np.array([5,6,7,8,9])\n",
    "\n",
    "---\n",
    "From array a remove all items present in array b\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "id": "eCNJXPvK9IAr"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,2,3,4,5]) \n",
    "b = np.array([5,6,7,8,9])\n",
    "c = np.setdiff1d(a, b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "gz4Dvd4b_Akh"
   },
   "source": [
    "38.  Following is the input NumPy array delete column two and insert following new column in its place.\n",
    "\n",
    "---\n",
    "sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) \n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "newColumn = numpy.array([[10,10,10]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "id": "lLWAJWJJ_I3d",
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[34 43 10]\n",
      " [82 22 10]\n",
      " [53 94 10]]\n"
     ]
    }
   ],
   "source": [
    "sampleArray = np.array([\n",
    "    [34,43,73],\n",
    "    [82,22,12],\n",
    "    [53,94,66]\n",
    "])\n",
    "newColumn = np.array([[10,10,10]])\n",
    "sampleArray = np.delete(sampleArray, 2, axis=1)\n",
    "sampleArray = np.insert(sampleArray, 2, newColumn, axis=1)\n",
    "print(sampleArray)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1lIfmbQt_J_W"
   },
   "source": [
    "39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])\n",
    "\n",
    "\n",
    "---\n",
    "Find the dot product of the above two matrix\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "id": "fV2-vXcR_vmu"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 28.  64.]\n",
      " [ 67. 181.]]\n"
     ]
    }
   ],
   "source": [
    "x = np.array([[1., 2., 3.], [4., 5., 6.]]) \n",
    "y = np.array([[6., 23.], [-1, 7], [8, 9]])\n",
    "print(np.dot(x,y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5U-4odUw_wP0"
   },
   "source": [
    "40. Generate a matrix of 20 random values and find its cumulative sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "id": "_oOHdiYEAF8N"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 18  25  27  33  48  55  59  62  73  88  96 114 130 143 159 171 187 189\n",
      " 201 210]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.uniform(1,20,size=(4,5))\n",
    "arr = arr.astype('int32')\n",
    "print(arr.cumsum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Numpy-Assignment-PIAIC-Batch35-Q2.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
