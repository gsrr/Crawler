#!/bin/bash
#!/bin/bash
./svm-scale -l -1 -u 1 -s range1 train.data > train.scale
./svm-train train.scale
