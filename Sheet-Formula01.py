=arrayformula
    (
        {UNIQUE
            (transpose
                (split
                    (join
                        (" , ",A1:A), " , ",false)
                )
              ),
if
    (istext
        (UNIQUE
             (transpose
                  (split
                       (join
                            (" , ",A1:A), " , ",false)
                  )
             )
        ),
countif
    (transpose
        (split
            (join(" , ",A1:A), " , ",false)
        ),
            UNIQUE
                (transpose
                    (split
                        (join(" , ",A1:A), " , ",false)))),)})