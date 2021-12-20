import numpy as np


# 1. exercise:

def calc_surface(array: list) -> int:
    # init surface value
    surface = 0

    # Looping through the elements of the list
    for n, x in enumerate(array):
        # adding top, bottom and sides to surface
        surface += 2*x + 2
        # adding the sides between the towers
        if n > 0:
            surface += abs(x - array[n-1])

    # adding the ends of the 3D structure to the surface
    surface += array[0] + array[-1]

    return surface


# 2. exercise

def queen_attack(n: int, r_q: int, c_q: int, obstacles: list) -> int:
    # init list of possible attacks
    steps = []
    # array of movement vectors
    vectors = np.array(
        [
            [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]
        ]
    )
    # queen start position
    start_cell = [r_q, c_q]
    # moving in the direction of vectors until reaching the end of the board
    for v in vectors:
        temp_pos = np.array(start_cell)
        while max(abs(temp_pos)) < n and min(abs(temp_pos)) > 1:
            # moving in the direction of vector
            temp_pos = np.add(temp_pos, v)
            # if the cell is not in obstacles add to possible cells
            if any(np.array_equal(x, temp_pos) for x in obstacles):
                break
            else:
                steps.append(temp_pos)

    # return the number of possible cells
    return len(steps)


# 3. exercise

def nxn_array(n: int) -> np.array:
    # generate nxn array of ones
    generated_array = np.ones([n, n])

    # change 1 to -1 based on j and i values
    for i, x in enumerate(generated_array):
        for j, y in enumerate(x):
            generated_array[i][j] *= pow(-1, i + j)

    return generated_array


# 4. exercise

def rowwise_norm(input_list: list) -> np.array:
    # transforming input list to numpy array
    input_np_array = np.array(input_list)

    # calculate the row-wise norm values of the input array
    norm_values = np.linalg.norm(input_np_array, axis=1)

    return norm_values


# 5. exercise

def matrices_to_diagonal(matrices: list) -> np.array:
    # Calculate size of output block matrix and initialize
    matrices = np.array(matrices)
    print(matrices)
    result_size = 0
    for m in matrices:
        result_size += len(m)
    block_matrix = np.zeros([result_size, result_size])

    # copying cell values from input matrices to output matrix
    cell_to_start = 0
    for m in matrices:
        m_size = len(m)                 # get size of current matrix
        for j, y in enumerate(m):       # rows
            for i, x in enumerate(y):   # columns
                block_matrix[cell_to_start + j][cell_to_start + i] = x  # add the input value to the output matrix
        cell_to_start += m_size         #

    return block_matrix


# 6. exercise

def calc_cookies(money: int, price: int, wrap: int, wrap_num=0) -> int:
    cookie_num = 0

    # Spend all the money for cookies (if possible), increase number of cookies and the number of wraps, decrease money
    if money >= price:
        cookies_bought = int(money / price)
        cookie_num += cookies_bought
        wrap_num += cookies_bought
        money -= cookies_bought * price

    # Spend all the wraps for cookies (if possible), increase number of cookies, decrease the number of wraps
    # + add the newly earned wraps to the number of wraps
    elif wrap_num >= wrap:
        cookies_from_wraps = int(wrap_num / wrap)
        cookie_num += cookies_from_wraps
        wrap_num -= cookies_from_wraps * wrap
        wrap_num += cookies_from_wraps

    else:
        # If we don't have enough money or wraps to get more cookies, the number of cookies=0
        return 0

    return cookie_num + calc_cookies(money=money, price=price, wrap=wrap, wrap_num=wrap_num)
