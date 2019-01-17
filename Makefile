input?=default-config.py
configpy=python $(input)
test_1_py=python test_1.py
test_2_py=python test_2.py

all: test_1.chk test_2.chk

test_1.chk: $(input)
	$(test_1_py) -i $(shell $(configpy) test_1/P_x) && \
		touch $@

test_2.chk: $(input)
	$(test_2_py) -i $(shell $(configpy) test_2/P_x) && \
		touch $@

