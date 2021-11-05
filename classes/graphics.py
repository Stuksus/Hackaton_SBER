class Grapher:
    def __init__(self, 
                 train, test=[], target_col = 'default_12m',
                 figsize = (10,5), target_colors = {0:'gray',1:'red'}
                 ):         

        self.df_original = (train,test)
        self.target = train[target_col]
        self.df = train.drop(columns=[target_col])
        self.dfs_by_target = [train[train[target_col]==target_value] for target_value in train[target_col].unique()]

        self.test = test

        self.plt_figsize = figsize
        self.plt_colored_target = self.target.map(target_colors)
        self.fplt_dims = {self.scatter:2,
                          self.scatter3d:3,
                          self.hist:1}
    
    def show_all(self,fplt):
        '''
        shows all possible fplt plots of df
        Example:
            g = Grapher( pd.DataFrame({a:[],b:[],c:[]}) )
            g.show_all(g.scatter) 
            -> 
            prints all possible scatter plots:
            g.scatter(a,b);g.scatter(a,c);g.scatter(b,c)
        !: 
            if many df columns then there are too many graphs to show
        '''

        from itertools import combinations as combi
        n=self.fplt_dims[fplt]

        for dims in combi(self.df.columns,n):
            fplt(*dims)

    def show_separate(self, fplt):
        '''
        should show 3 fplt plots side by side: 
        {{default+alive,default,alive}}

        In general should show n+1 fplt plots side by side:
        {{everething, target_group_1, target_group_2, ... , target_group_n}}
        '''
        # all = self.df
        # dead = all[self.target == 1]
        # alive = all[all[self.target != 1]

        # all = Grapher(train=all)
        # dead = Grapher(train=dead)
        # alive = Grapher(train=alive)

        # all.scatter3d()
        # dead.scatter3d()
        # alive.scatter3d()
        pass
    
    def scatter(self,
                x_name = 'bus_age', y_name = 'ul_capital_sum',
                alpha = 0.3,
                xscale = 'linear',
                yscale = 'linear'
                ):
        
        fig, ax = plt.subplots(figsize=self.plt_figsize)

        ax.scatter(
                x = self.df[x_name], 
                y = self.df[y_name], 
                c = self.plt_colored_target,
                alpha = alpha
                )
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)
        plt.xlabel(x_name)
        plt.ylabel(y_name)

        plt.show()

    def scatter3d(self,
                  x_name='ul_capital_sum',
                  y_name='ul_founders_cnt',
                  z_name='bus_age',
                  alpha = 0.3,
                  xscale = 'linear',
                  yscale = 'linear',
                  zscale = 'linear'):
        
        fig = plt.figure(figsize=self.plt_figsize)
        ax = fig.add_subplot(projection='3d')

        ax.scatter(self.df[x_name], 
                   self.df[y_name], 
                   self.df[z_name], 
                   c = self.plt_colored_target,
                   alpha = alpha)
        
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)
        ax.set_zscale(zscale)
        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        ax.set_zlabel(z_name)

        plt.show()

    def hist(self, n_bins = 10):
        pass
