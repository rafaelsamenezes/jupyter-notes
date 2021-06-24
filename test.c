int foo(int c) {
        int a = 0;
        int b;
    L1: 
        b = a + 1;

        c = c + b;
        a = b * 2;
        if (a < 9) 
            goto L1;
        return c;
}