class StandardScaler2 :

    def __init__ (self):
        
        self.params_ = {}        

    def fit (self, numpy_array) :

      self.numpy_array = numpy_array

      if type(self.numpy_array) == "pandas.core.frame.DataFrame" :

        self.numpy_array = numpy_array.values
        self.moyenne = np.mean(self.numpy_array,axis = 0)
        self.ecart_type = np.std(self.numpy_array,axis = 0)  

        self.params_ ["moyenne"] = self.moyenne
        self.params_ ["ecart_type"] = self.ecart_type

        return(self.params_)      
        
      else :
        
        self.moyenne = np.mean(self.numpy_array,axis = 0)
        self.ecart_type = np.std(self.numpy_array,axis = 0)  

        self.params_ ["moyenne"] = self.moyenne
        self.params_ ["ecart_type"] = self.ecart_type

        return(self.params_)

    def fit_transform (self, numpy_array) :
      
      try:

        self.fit_transform = ( self.numpy_array - self.moyenne ) / self.ecart_type
        return(self.fit_transform)
        
      except AttributeError:

        raise ValueError ("ecart_type and moyenne not found, try fit method prior to fit_transform")

    def transform (self):

      self.transform = ( self.numpy_array - self.moyenne ) / self.ecart_type