test = {
  'name': 'Question 20',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (analyze 1)
          1
          scm> (analyze 'a)
          a
          scm> (analyze '(+ 1 2))
          (+ 1 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (analyze '(quote (let ((a 1) (b 2)) (+ a b))))
          (quote (let ((a 1) (b 2)) (+ a b)))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (analyze '(lambda (let a b) (+ let a b)))
          (lambda (let a b) (+ let a b))
          scm> (analyze '(lambda (x) a (let ((a x)) a)))
          (lambda (x) a ((lambda (a) a) x))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (analyze '(let ((a 1)
          ....                 (b 2))
          ....                (+ a b)))
          ((lambda (a b) (+ a b)) 1 2)
          scm> (analyze '(let ((a (let ((a 2)) a))
          ....                 (b 2))
          ....                (+ a b)))
          ((lambda (a b) (+ a b)) ((lambda (a) a) 2) 2)
          scm> (analyze '(let ((a 1))
          ....                (let ((b a))
          ....                     b)))
          ((lambda (a) ((lambda (b) b) a)) 1)
          scm> (analyze '(+ 1 (let ((a 1)) a)))
          (+ 1 ((lambda (a) a) 1))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}