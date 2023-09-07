
class unit_converter:
    def __init__(self,unit_from,unit_to,value_from):
        self.unit_from=unit_from
        self.unit_to=unit_to
        self.value_from=value_from
    
    def __cnvcm(self):
        result=0
        if self.unit_to=='centimeter':
            result=self.value_from
        elif self.unit_to=='meter':
            result=self.value_from/100
        elif self.unit_to=='kilometer':
            result=self.value_from/100000
        elif self.unit_to=='mile':
            result=self.value_from* 0.010936132983
        elif self.unit_to=='yard':
            result=self.value_from*6.2

        return result
    
    def __cnv_meters(self):
        result=0
        if self.unit_to=='centimeter':
            result=self.value_from*100
        elif self.unit_to=='meter':
            result=self.value_from
        elif self.unit_to=='kilometer':
            result=self.value_from/1000
        elif self.unit_to=='mile':
            result=self.value_from*0.0006
        elif self.unit_to=='yard':
            result=self.value_from*1.09
        return result



    def cnvunits(self):
        if self.unit_from=='centimeter':
            return self.__cnvcm()
        elif self.unit_from=='meter':
            return self.__cnv_meters()