import numpy as np


def get_popularity_score(member_item_matrix):
    """
    人気スコア: ユーザーごとの商品の興味行列に基づいてスコアを算出

    以下のような行=user, 列=商品の2次元配列のユーザーごとの商品の嗜好を元にスコアを出力
    member_item_matrix = np.array([
        [10., 0., 2., 1., 0.],
        [10., 0., 2., 1., 0.],
        [3., 1., 0., 0., 3.],
        [10., 0., 1., 0., 2.]
    ])
    :param member_item_matrix: 会員(行) x 商品(列) のmatrix, dtype = int8を想定
    :type member_item_matrix: scipy.sparse.csr_matrix (row based sparse matrix)
    :return: 列ごとにsumした数値の行列。 1行 x 商品数分の列
    :rtype: numpy.ndarray (dtype=np.float32)
    """
    return member_item_matrix.sum(axis=0, dtype=np.float32)
