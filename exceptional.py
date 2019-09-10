import sys

def convert(s) :
    '''Convert to int'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion error :{}'.format(e), file=sys.stderr)
        raise
