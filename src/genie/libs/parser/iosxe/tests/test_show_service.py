# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_service import ShowServiceGroupStats


# ============================================
# Parser for 'show service-group stats'
# ============================================
class test_show_service_group_stats(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {
        'service_group_statistics':{
            'global': {
                'num_of_groups' : 5,
                'num_of_members' : 8005
            },
            '1' : {
                'num_of_interfaces' : 1,
                'num_of_members' : {
                    3000 : {
                        'service_instance': 3000
                    }
                },
                'members_joined': 13000,
                'members_left': 10000
            },
            '2' : {
                'num_of_interfaces' : 1,
                'num_of_members' : {
                    2000 : {
                        'service_instance': 2000
                    }
                },
                'members_joined': 10000,
                'members_left': 8000
            },
            '3' : {
                'num_of_interfaces' : 1,
                'num_of_members' : {
                    3000 : {
                        'service_instance': 3000
                    }
                },
                'members_joined': 9000,
                'members_left': 6000
            },
            '10' : {
                'num_of_interfaces' : 1,
                'num_of_members' : {
                    3 : {
                        'service_instance': 3
                    }
                },
                'members_joined': 8003,
                'members_left': 8000
            },
            '20' : {
                'num_of_interfaces' : 1,
                'num_of_members' : {
                    2 : {
                        'service_instance': 2
                    }
                },
                'members_joined': 8002,
                'members_left': 8000
            }
        }
    }
    golden_parsed_output_2 = {
        'service_group_statistics':{
            'global': {
                'num_of_groups' : 1,
                'num_of_members' : 2
            },
            '1' : {
                'num_of_interfaces' : 1,
                'num_of_members' : {
                    2 : {
                        'sub_interface': 2
                    }
                },
                'members_joined': 103,
                'members_left': 101
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Service Group global statistics:
          Number of groups:                       5
          Number of members:                      8005
        Service Group 1 statistics:
          Number of Interfaces:                   1
          Number of members:                      3000
            Service Instance                      3000
          Members joined:                         13000
          Members left:                           10000
        Service Group 2 statistics:
          Number of Interfaces:                   1
          Number of members:                      2000
            Service Instance                      2000
          Members joined:                         10000
          Members left:                           8000
        Service Group 3 statistics:
          Number of Interfaces:                   1
          Number of members:                      3000
            Service Instance                      3000
          Members joined:                         9000
          Members left:                           6000
        Service Group 10 statistics:
          Number of Interfaces:                   1
          Number of members:                      3
            Service Instance                      3
          Members joined:                         8003
          Members left:                           8000
        Service Group 20 statistics:
          Number of Interfaces:                   1
          Number of members:                      2
            Service Instance                      2
          Members joined:                         8002
          Members left:                           8000
    '''}

    golden_output_2 = {'execute.return_value': '''\
        Service Group global statistics:
          Number of groups:                       1
          Number of members:                      2
        Service Group 1 statistics:
          Number of Interfaces:                   1
          Number of members:                      2
            Sub-interface                         2
          Members joined:                         103
          Members left:                           101
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowServiceGroupStats(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowServiceGroupStats(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowServiceGroupStats(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()