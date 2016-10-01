#lang planet neil/sicp
(define (sum-intergers a b)
  (if (> a b)
      0
      (+ a (sum-intergers (+ a 1) b))))
(define (cube x) (* x x x))
(define (sum-cubes a b)
       (if (> a b)
           0
           (+ (cube a) (sum-cubes (+ a 1) b))))

(define (sum term a next b)
        (if (> a b)
            0
            (+ (term a)
               (sum term (next a) next b))))
(define (inc n) (+ n 1))
(define (sum-cube a b)
        (sum cube a inc b))

(define (pi-sum a b)
        (define (pi-term x)
                (/ 1.0 (* x (+ x 2))))
        (define (pi-next x)
                (+ x 4))
        (sum pi-term a pi-next b))

(define pi (* 8 (pi-sum 1 10000)))
