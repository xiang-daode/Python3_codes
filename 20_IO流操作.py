#!/usr/bin/python
# -*- coding: cp936 -*-


import io

output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()
print(contents )



# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
print('output closed !')



