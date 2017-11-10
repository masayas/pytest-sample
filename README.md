# pytest-sample

これはpytestのサンプルを書いておくRepository

## Dependencies

- Python 3.6
- pytest==3.2.3
- pytest-pythonpath==0.7.1
- pytest-cov==2.5.1

## Setup

- 環境を設定: $ conda env create -f environment.yml
- venvをactivate: $ source activate pytest-sample

## How to run pytest

- test_xxxx.py というテストモジュールを自動的に探してテストを開始するので、tests directoryで以下のコマンドを実行

### Run without coverage

$ python -m pytest 

### Run with coverage 

$ python -m pytest --cov-report=term --cov=test_main

## ユニットテスト

### ユニットテストとは

- ユニット=塊。
- なんの塊をテストするかはチームで決める。xUnitパターンとか読んで勉強すればよい。
- 今回の対象はあくまでもバッチ処理などで使われる関数などのテストで、Webは対象ではない(webtestなどいろんなものがある)
- テストの距離

  - テストで直接対象のAPIを呼ぶ（距離1）
  - APIを使っているview関数等を呼ぶ（距離N）
  - 距離が遠いとテストケースが複雑になる

    - 細かいテスト（ユニットテスト）を積み上げるのが基本パターン

### 基本ルール

  - 関数単位でテストしましょう。
  - inputとoutputを明確にしましょう。
  - それを通るように実装しましょう。
  - 不必要に複雑なテストは要らない、そのため不要になったテストコードはドンドン消して負債を減らす

### pytestの基本

1. テスト対象はfixtureデコレーターで囲み、target関数とする

例:
```@pytest.fixture
    def target(self):
        from main import add 
        return add```

2. test時には対象をcall, そしてassertして検証するだけのようなテストにする

例:
```
    def test_addint(self, target):
        # call
        actual = target(1, 2)

        # verify
        expect = 3
        assert actual == expect
```
3. 複数ケースのテストの場合は、parametrizeをつかうのはよい

4. テスト対象ではない、しかし依存関係のあるclassなどは、patch デコレーターでpatchを当てるとテストしやすい

### pytestとは

- pytest

  - 失敗時はテストコードも表示してくれるので結果が見やすい。
  - unittest.TestCaseを継承する必要がない。

    - assertEqualが使えなくなる。
    - assert で十分になる。

  - parametrize が使える。

    - for文を書かなくてもよくなる
    - 入力値毎に別のテストケースとして実行できる。

      - unittest だと for 文内の assert は 1テスト扱い。

  - fixture が使える。
  - test_で始まる関数ならテストとして認識してくれる。
  - dict型やlist型等にも対応。

    - -v, -vvオプションでどこがエラーか詳細が表示される。

### 参考: Python における色んなユニットテスト

- doctest

  - 一番単純。
  - 実装に書いてあるので、利用者にとって分かりやすい。
  - 複雑なテストには向かない。(import 文とか書き出すと...)
  - ドキュメントに書いてあるヘルプが実装と乖離していないかをチェックするため。
  - ドキュメントのテストと考えてもよい。

  - 例: 

  ```
    def add(a, b):
        """
        この関数は a + b の結果を返します
        例:

        >>> add(1, 2)
        3

        >>> add('abc', 'def')
        'abcdef'

        以上
        """
        return a + b
  ```

  - 実行例:
  
  ```
  $ python -m doctest main.py -v
      Trying:
          add(1, 2)
      Expecting:
          3
      ok
      Trying:
          add('abc', 'def')
      Expecting:
          'abcdef'
      ok
      1 items had no tests:
          main
      1 items passed all tests:
         2 tests in main.add
      2 tests in 2 items.
      2 passed and 0 failed.
      Test passed.
  ```

- assert 文

  - AsseriionErrorの内容が分かりにくい

- assertEqual

  - AssertionErrorの内容が assert 文より分かりやすい

## Reference

- [Pythonプロフェッショナルプログラミング第2版 by (株)ビープラウド](https://www.amazon.co.jp/Python%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E7%AC%AC2%E7%89%88-%E3%83%93%E3%83%BC%E3%83%97%E3%83%A9%E3%82%A6%E3%83%89/dp/479804315X/ref=pd_lpo_sbs_14_t_2?_encoding=UTF8&psc=1&refRID=7P2EJ54962KTTQG5J58Y) 8章
  モジュール分割設計と単体テスト

- [[Python] 初中級者のためのpytest入門](http://note.crohaco.net/2016/python-pytest/)
