x = [0	0	0	0	0	0
0	0	0	0	0	1
0	0	0	0	1	0
0	0	0	0	1	1
0	0	0	1	0	0
0	0	0	1	0	1
0	0	0	1	1	0
0	0	0	1	1	1
0	0	1	0	0	0
0	0	1	0	0	1
0	0	1	0	1	0
0	0	1	0	1	1
0	0	1	1	0	0
0	0	1	1	0	1
0	0	1	1	1	0
0	0	1	1	1	1
0	1	0	0	0	0
0	1	0	0	0	1
0	1	0	0	1	0
0	1	0	0	1	1
0	1	0	1	0	0
0	1	0	1	0	1
0	1	0	1	1	0
0	1	0	1	1	1
0	1	1	0	0	0
0	1	1	0	0	1
0	1	1	0	1	0
0	1	1	0	1	1
0	1	1	1	0	0
0	1	1	1	0	1
0	1	1	1	1	0
0	1	1	1	1	1
1	0	0	0	0	0
1	0	0	0	0	1
1	0	0	0	1	0
1	0	0	0	1	1
1	0	0	1	0	0
1	0	0	1	0	1
1	0	0	1	1	0
1	0	0	1	1	1
1	0	1	0	0	0
1	0	1	0	0	1
1	0	1	0	1	0
1	0	1	0	1	1
1	0	1	1	0	0
1	0	1	1	0	1
1	0	1	1	1	0
1	0	1	1	1	1
1	1	0	0	0	0
1	1	0	0	0	1
1	1	0	0	1	0
1	1	0	0	1	1
1	1	0	1	0	0
1	1	0	1	0	1
1	1	0	1	1	0
1	1	0	1	1	1
1	1	1	0	0	0
1	1	1	0	0	1
1	1	1	0	1	0
1	1	1	0	1	1
1	1	1	1	0	0
1	1	1	1	0	1
1	1	1	1	1	0
1	1	1	1	1	1]


y = [x(:,2:6)  bitxor( x(:,1), bitand(x(:,2),x(:,3)))]

[r, c] = size(x)


count = 0
for i=1:r
    before = count;
    for j = 1:r
        if sum( x(i,:) == y(j,:) ) == 6
            count = count + 1;
        end
    end
    after(i) = count - before;
end
after
count
