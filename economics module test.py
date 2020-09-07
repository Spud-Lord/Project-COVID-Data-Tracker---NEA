#Jake Eaton

from economics import Inflation
import datetime

inflation = Inflation()

usa_2007 = Inflation(reference=datetime.date(2007,1,1), country = 'United States')

usa_2007.get(datetime.date(2011,1,1))
