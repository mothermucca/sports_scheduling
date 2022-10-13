# hack to capture stdout to a string, to test it
import os
import re
import subprocess
import sys
from contextlib import contextmanager


@contextmanager
def redirected(out=sys.stdout, err=sys.stderr):
    saved = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        yield
    finally:
        sys.stdout, sys.stderr = saved


# noinspection PyBroadException
def test_edge_cases():
    output_file = 'jabba'
    try:
        # clean up the temp file
        os.unlink(output_file + '.csv')
        os.unlink(output_file + '_1.csv')
        os.unlink(output_file + '_2.csv')
    except:
        pass

    # test adding csv to ending of output file
    process_command_line = ['python', 'src/sports_schedule_sat.py'
        , '-t', '8'
        , '-d', '14'
        , '-p', '2'
        , '--debug'
        , '--timelimit', '10'
        , '--csv', output_file]
    try:
        proc = subprocess.run(process_command_line, encoding='utf8', capture_output=True)
        out = proc.stdout
        err = proc.stderr
        print('out is ', out)
        # assert re.search('OPTIMAL', out, re.MULTILINE)
        assert not os.path.isfile(output_file)
        assert os.path.isfile(output_file + '.csv')
        assert not os.path.isfile(output_file + '_1.csv')
        assert not os.path.isfile(output_file + '_2.csv')
    except:
        assert False

    # test adding _1.csv to ending of output file if it already exists
    process_command_line = ['python', 'src/sports_schedule_sat.py'
        , '-t', '8'
        , '-d', '14'
        , '-p', '2'
        , '--debug'
        , '--timelimit', '10'
        , '--csv', output_file]
    try:
        proc = subprocess.run(process_command_line, encoding='utf8', capture_output=True)
        out = proc.stdout
        err = proc.stderr
        print('out is ', out)
        assert re.search('OPTIMAL', out, re.MULTILINE)
        assert not os.path.isfile(output_file)
        assert os.path.isfile(output_file + '.csv')
        assert os.path.isfile(output_file + '_1.csv')
        assert not os.path.isfile(output_file + '_2.csv')
    except:
        assert False
    # test adding _2.csv to ending of output file if it already exists
    process_command_line = ['python', 'src/sports_schedule_sat.py'
        , '-t', '8'
        , '-d', '14'
        , '-p', '2'
        , '--debug'
        , '--timelimit', '10'
        , '--csv', output_file]
    try:
        proc = subprocess.run(process_command_line, encoding='utf8', capture_output=True)
        out = proc.stdout
        err = proc.stderr
        print('out is ', out)
        assert re.search('OPTIMAL', out, re.MULTILINE)
        assert not os.path.isfile(output_file)
        assert os.path.isfile(output_file + '.csv')
        assert os.path.isfile(output_file + '_1.csv')
        assert os.path.isfile(output_file + '_2.csv')
    except:
        assert False

    try:
        # clean up the temp file
        os.unlink(output_file + '.csv')
        os.unlink(output_file + '_1.csv')
        os.unlink(output_file + '_2.csv')
    except:
        pass
