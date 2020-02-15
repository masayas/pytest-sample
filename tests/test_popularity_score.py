import numpy as np
from scipy import sparse
import numpy.testing as npt

from unittest.mock import patch
import pytest


class TestGetPopularityScore:
    """人気スコアモデルのテストケース"""

    @pytest.fixture
    def member_item_matrix(self):
        # userの商品閲覧履歴のarray
        # 各行=user,
        # 各列=商品に対する興味行列 (最も大きい数値のみが入る)
        #  0 = 未アクセス
        #  1 = 1回だけアクセス
        #  2 = 2回以上アクセス
        #  3 = リクエスト済み
        # 10 = 購買済み
        member_item_matrix = np.array([
            [10., 0., 2., 1., 0.],
            [10., 0., 2., 1., 0.],  # user１とuser2の興味行列はわざと同じもの
            [3., 1., 0., 0., 3.],
            [10., 0., 1., 0., 2.]
        ], dtype=np.int8)
        return sparse.csr_matrix(member_item_matrix)

    @pytest.fixture
    def expected_popularity_score(self):
        return np.array([[33, 1, 5, 2, 5]], dtype=np.float32)

    @pytest.fixture
    def target(self):
        from src.popularity_score import get_popularity_score
        return get_popularity_score

    def test_it(self, target, member_item_matrix, expected_popularity_score):
        """
        人気スコアがただしいか
        """
        target = target(member_item_matrix)
        assert target.dtype == np.dtype('float32')
        npt.assert_array_equal(target, expected_popularity_score)
