'''
IOSXR parsers for the following commands:
    * show processes isis
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

class ShowProcessesIsisSchema(MetaParser):
    ''' Schema for commands:
        * show processes isis
    '''
    schema = {
        'job_id': {
            Any(): {
                'pid': int,
                'process_name': str,
                'executable_path': str,
                'instance': str,
                'version_id': str,
                'respawn': str,
                'respawn_count': int,
                'last_started': str,
                'process_state': str,
                'package_state': str,
                'started_on_config': str,
                'process_group': str,
                'core': str,
                'max_core': str,
                'placement': str,
                'startup_path': str,
                'ready': str,
                'available': str,
                'process_cpu_time': {
                    'user': str,
                    'kernel': str,
                    'total': str,
                },
                'processes': {
                    'tid': {
                        Any(): {
                            'stack': str,
                            'pri': int,
                            'state': str,
                            'name': str,
                            'rt_pri': int,
                        }
                    }
                }
            }
        }
    }

class ShowProcessesIsis(ShowProcessesIsisSchema):
    ''' Parser for:
        * 'show processes isis'
    '''

    cli_command = 'show processes isis'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_output = {}

        # Job Id: 1011
        r1 = re.compile(r'Job\s+Id\s*:\s*(?P<job_id>\d+)')

        # PID: 22464
        r2 = re.compile(r'PID\s*:\s*(?P<pid>\d+)')

        # Process name: isis
        r3 = re.compile(r'Process\s+name\s*:\s+(?P<process_name>\S+)')

        # Executable path: /opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/bin/isis
        r4 = re.compile(r'Executable\s+path\s*:\s*(?P<executable_path>\S+)')

        # Instance #: 1
        r5 = re.compile(r'Instance\s+\#\s*:\s*(?P<instance_number>\d+)')

        # Version ID: 00.00.0000
        r6 = re.compile(r'Version\s+ID\s*:\s*(?P<version_id>\S+)')

        # Respawn: ON
        r7 = re.compile(r'Respawn\s*:\s*(?P<respawn>(ON|OFF))')

        # Respawn count: 1
        r8 = re.compile(r'Respawn\s+count\s*:\s*(?P<respawn_count>\d+)')

        # Last started: Wed Jan 30 20:43:04 2019
        r9 = re.compile(r'Last\s+started\s*:\s*(?P<last_started>.+)')

        # Process state: Run
        r10 = re.compile(r'Process\s+state\s*:\s*(?P<process_state>.+)')

        # Package state: Normal
        r11 = re.compile(r'Package\s+state\s*:\s*(?P<package_state>.+)')

        # Started on config: cfg/gl/isis/instance/test/ord_A/running
        r12 = re.compile(r'Started\s+on\s+config\s*:\s*'
                          '(?P<started_on_config>\S+)')

        # Process group: v4-routing
        r13 = re.compile(r'Process\s+group\s*:\s*(?P<process_group>\S+)')

        # core: COPY
        r14 = re.compile(r'core\s*:\s*(?P<core>\S+)')

        # Max. core: 0
        r15 = re.compile(r'Max\.\s+core\s*:\s*(?P<max_core>\d+)')

        # Placement: Placeable
        r16 = re.compile(r'Placement\s*:\s*(?P<placement>.+)')

        # startup_path: /opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/startup/isis.startup
        r17 = re.compile(r'startup\_path\s*:\s*(?P<startup_path>\S+)')

        # Ready: 1.804s
        r18 = re.compile(r'Ready\s*:\s*(?P<ready>.+)')

        # Available: 1.892s
        r19 = re.compile(r'Available\s*:\s*(?P<available>.+)')

        # Process cpu time: 2.690 user, 0.640 kernel, 3.330 total
        r20 = re.compile(r'Process\s+cpu\s+time\s*:\s*(?P<cpu_time_user>\S+)'
                          '\s+user,\s+(?P<cpu_time_kernel>\S+)\s+kernel,\s+'
                          '(?P<cpu_time_total>\S+)\s+total')

        # JID    TID   Stack  pri  state        NAME             rt_pri
        # 1011   22511    0K  20   Sleeping     Decision         0
        # 1011   22512    0K  20   Sleeping     TE               0
        # 1011   22513    0K  20   Sleeping     MIB Traps        0
        # 1011   22514    0K  20   Sleeping     Protect Infra    0
        # 1011   22494    0K  20   Sleeping     telemetry_evtli  0
        # 1011   22487    0K  20   Sleeping     lspv_lib ISIS    0
        r21 = re.compile(r'(?P<jid>\d+)\s+(?P<tid>\d+)\s+(?P<stack>\S+)\s+'
                          '(?P<pri>\d+)\s+(?P<state>\S+)\s+\s'
                          '(?P<name>[\sa-zA-Z\_\-]+)\s+(?P<rt_pri>\d+)')

        for line in output.splitlines():
            line = line.strip()

            # Job Id: 1011
            result = r1.match(line)
            if result:
                group = result.groupdict()
                job_id = group['job_id']
                job_dict = parsed_output\
                    .setdefault('job_id', {})\
                    .setdefault(job_id, {})\

                continue

            # PID: 22464
            result = r2.match(line)
            if result:
                group = result.groupdict()
                pid = int(group['pid'])

                job_dict['pid'] = pid

                continue

            # Process name: isis
            result = r3.match(line)
            if result:
                group = result.groupdict()
                process_name = group['process_name']

                job_dict['process_name'] = process_name

                continue

            # Executable path: /opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/bin/isis
            result = r4.match(line)
            if result:
                group = result.groupdict()
                executable_path = group['executable_path']

                job_dict['executable_path'] = executable_path

                continue

            # Instance #: 1            
            result = r5.match(line)
            if result:
                group = result.groupdict()
                instance_number = group['instance_number']

                job_dict['instance'] = instance_number

                continue

            # Version ID: 00.00.0000            
            result = r6.match(line)
            if result:
                group = result.groupdict()
                version_id = group['version_id']

                job_dict['version_id'] = version_id

                continue

            # Respawn: ON
            result = r7.match(line)
            if result:
                group = result.groupdict()
                respawn = group['respawn']

                job_dict['respawn'] = respawn

                continue

            # Respawn count: 1
            result = r8.match(line)
            if result:
                group = result.groupdict()
                respawn_count = int(group['respawn_count'])

                job_dict['respawn_count'] = respawn_count

                continue

            # Last started: Wed Jan 30 20:43:04 2019            
            result = r9.match(line)
            if result:
                group = result.groupdict()
                last_started = group['last_started']

                job_dict['last_started'] = last_started

                continue

            # Process state: Run
            result = r10.match(line)
            if result:
                group = result.groupdict()
                process_state = group['process_state']

                job_dict['process_state'] = process_state

                continue

            # Package state: Normal            
            result = r11.match(line)
            if result:
                group = result.groupdict()
                package_state = group['package_state']

                job_dict['package_state'] = package_state

                continue

            # Started on config: cfg/gl/isis/instance/test/ord_A/running            
            result = r12.match(line)
            if result:
                group = result.groupdict()
                started_on_config = group['started_on_config']

                job_dict['started_on_config'] = started_on_config

                continue

            # Process group: v4-routing
            result = r13.match(line)
            if result:
                group = result.groupdict()
                process_group = group['process_group']

                job_dict['process_group'] = process_group

                continue

            # core: COPY            
            result = r14.match(line)
            if result:
                group = result.groupdict()
                core = group['core']

                job_dict['core'] = core

                continue

            # Max. core: 0            
            result = r15.match(line)
            if result:
                group = result.groupdict()
                max_core = group['max_core']

                job_dict['max_core'] = max_core

                continue

            # Placement: Placeable
            result = r16.match(line)
            if result:
                group = result.groupdict()
                placement = group['placement']

                job_dict['placement'] = placement

                continue

            # startup_path: /opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/startup/isis.startup            
            result = r17.match(line)
            if result:
                group = result.groupdict()
                startup_path = group['startup_path']

                job_dict['startup_path'] = startup_path

                continue

            # Ready: 1.804s            
            result = r18.match(line)
            if result:
                group = result.groupdict()
                ready = group['ready']

                job_dict['ready'] = ready

                continue

            # Available: 1.892s            
            result = r19.match(line)
            if result:
                group = result.groupdict()
                available = group['available']

                job_dict['available'] = available

                continue

            # Process cpu time: 2.690 user, 0.640 kernel, 3.330 total
            result = r20.match(line)
            if result:
                group = result.groupdict()
                cpu_time_user = group['cpu_time_user']
                cpu_time_kernel = group['cpu_time_kernel']
                cpu_time_total = group['cpu_time_total']

                process_cpu_time_dict = job_dict\
                    .setdefault('process_cpu_time', {})

                process_cpu_time_dict['user'] = cpu_time_user
                process_cpu_time_dict['kernel'] = cpu_time_kernel
                process_cpu_time_dict['total'] = cpu_time_total

                continue

            # JID    TID   Stack  pri  state        NAME             rt_pri
            # 1011   22511    0K  20   Sleeping     Decision         0
            # 1011   22512    0K  20   Sleeping     TE               0
            # 1011   22513    0K  20   Sleeping     MIB Traps        0
            # 1011   22514    0K  20   Sleeping     Protect Infra    0
            # 1011   22494    0K  20   Sleeping     telemetry_evtli  0
            # 1011   22487    0K  20   Sleeping     lspv_lib ISIS    0
            result = r21.match(line)
            if result:
                group = result.groupdict()
                jid = group['jid']
                tid = int(group['tid'])
                stack = group['stack']
                pri = int(group['pri'])
                state = group['state']
                name = group['name'].strip()
                rt_pri = int(group['rt_pri'])

                processes_dict = parsed_output\
                    .setdefault('job_id', {})\
                    .setdefault(jid, {})\
                    .setdefault('processes', {})\
                    .setdefault('tid', {})\
                    .setdefault(tid, {})

                processes_dict['stack'] = stack
                processes_dict['pri'] = pri
                processes_dict['state'] = state
                processes_dict['name'] = name
                processes_dict['rt_pri'] = rt_pri

                continue

        return parsed_output
