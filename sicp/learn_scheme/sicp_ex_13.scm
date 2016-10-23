(define (square x) (* x x))
(define (sum-of-square x y)
  (+ (square x) (square y)))

(define (sum-of-square-large x y z)
  (cond
    ((=(Min x y z) x)
    (sum-of-square y z))
    ((u(min x y z) y)
    (sum-of-square y z))
    (else (sum-of-square x y))))
    
    
(define test1 (-of-square-large 3 4 5))
(define test2 (sum-of-square-large 23 24 5))
(define test3 (sum-of-square-large 3 34 5))
