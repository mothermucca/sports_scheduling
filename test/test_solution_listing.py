# hack to capture stdout to a string, to test it
import filecmp
import os
import re
import subprocess


def test_solution_listing():
    # now for various combinations of inputs
    output_file = 'test/data/list_output_t4_d3_p1.csv'

    # test writing a list of solutions
    process_command_line = ['python', 'src/sports_schedule_sat.py'
        , '-t', '4'
        , '-d', '3'
        , '-p', '1'
        , '--debug'
        , '--timelimit', '10'
        , '--csv', output_file
        , '--enumerate']
    try:
        proc = subprocess.run(process_command_line, encoding='utf8', capture_output=True)
        out = proc.stdout
        err = proc.stderr
        assert re.search(r"^day=\d, home=\d, away=\d, home pool=\d, away pool=\d$",
                         out, re.MULTILINE)
        assert re.search(r"#144", out, re.MULTILINE)
        assert not re.search(r"#145", out, re.MULTILINE)
        assert re.search('OPTIMAL', out, re.MULTILINE)
        expected_file = 'test/data/list_output_t4_d3_p1.csv'
        assert filecmp.cmp(output_file, expected_file) is not None
    except:
        assert False

    try:
        # clean up the temp file
        os.unlink(output_file)
    except:
        print('no file to delete')

    output_file = 'test/data/list_output_t4_d2_p2.csv'
    # test writing a list of solutions, not a round-robin case
    process_command_line = ['python', 'src/sports_schedule_sat.py'
        , '-t', '4'
        , '-d', '2'
        , '-p', '2'
        , '--debug'
        , '--timelimit', '10'
        , '--csv', output_file
        , '--enumerate']
    try:
        proc = subprocess.run(process_command_line, encoding='utf8', capture_output=True)
        out = proc.stdout
        err = proc.stderr
        assert re.search('#24', out, re.MULTILINE)
        assert not re.search('#25', out, re.MULTILINE)
        assert re.search('OPTIMAL', out, re.MULTILINE)
        expected_file = 'test/data/list_output_t4_d2_p2.csv'
        assert filecmp.cmp(output_file, expected_file) is not None
    except:
        assert False

    try:
        # clean up the temp file
        os.unlink(output_file)
    except:
        print('no file to delete')
