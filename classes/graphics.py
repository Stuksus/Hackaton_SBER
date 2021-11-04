class Grapher:
    def __init__(self, 
                 train, test=[], target_col = 'default_12m',
                 figsize = (8,4), target_colors = {0:'gray',1:'red'}
                 ):         

        self.df_original = (train,test)
        self.target = train[target_col]
        self.df = train.drop(columns=[target_col])

        self.test = test

        self.plt_figsize = figsize
        self.plt_colored_target = self.target.map(target_colors)
        self.fplt_dims = {self.scatter:2,
                          self.scatter3d:3,
                          self.hist:1}
    
    def show_all(self,f_plt):
        '''
        shows all possible f_plt plots of df
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
        n=self.fplt_dims[f_plt]

        for dims in combi(self.df.columns,n):
            f_plt(*dims)

    def scatter(self,
                x_name = 'ar_management_expenses', y_name = 'ar_net_profit',
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

    def scatter3d(self):
        pass

    def hist(self, n_bins = 10):
        pass
