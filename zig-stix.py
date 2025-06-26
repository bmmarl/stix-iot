from stix2 import Bundle, parse, ExtensionDefinition
import stix2
import json
import uuid
from uuid import uuid5

SCO_DET_ID_NAMESPACE = uuid.UUID('00abedb4-aa42-466c-9c01-fed23315a9b7')
def gen_uuid(string,name):
    return f'{string}--{uuid.uuid5(SCO_DET_ID_NAMESPACE,name)}'


ext_defs = list()

iot_device_def = ExtensionDefinition(
        id=gen_uuid("extension-definition","iot_device_def"),
        created_by_ref=gen_uuid("identity", "id"),
        name="iot-infrastrucutre",
        description="This extension creates a new SDO that can be used to represent IoT devices, sensors, hubs, etc.",
        schema="https://raw.githubusercontent.com/bmmarl/stix-iot/refs/heads/main/STIG/src/static/jsedit/iot-infrastructure.json",
        version="1.0",
        extension_types=[
    	    "new-sdo"
        ])
ext_defs.append(iot_device_def)

iot_traffic_def = ExtensionDefinition(
        id=gen_uuid("extension-definition", "iot_traffic_def"),
        created_by_ref=gen_uuid("identity", "id"),
        name="iot-traffic",
        description="This extension creates a new SCO that can be used to represent traffic between IoT Devices, specifically under the IEEE 803.15.4 standard and ZigBee protcol.",
        schema="https://raw.githubusercontent.com/bmmarl/stix-iot/refs/heads/main/STIG/src/static/jsedit/observables/iot-traffic.json",
        version="1.0",
        extension_types=[
            "new-sco"
        ])
ext_defs.append(iot_traffic_def)

zbee_nwk_addr_def = ExtensionDefinition(
        id=gen_uuid("extension-definition", "zbee_nwk_addr_def"),
        created_by_ref=gen_uuid("identity", "id"),
        name="zbee-nwk-addr",
        description="This extension creates a new SCO that can be used to represent 16 Bit network Zigbee Addresses for IoT Devices",
        schema="https://raw.githubusercontent.com/bmmarl/stix-iot/refs/heads/main/STIG/src/static/jsedit/observables/zbee-nwk-addr.json",
        version="1.0",
        extension_types=[
            "new-sco"
        ])
ext_defs.append(zbee_nwk_addr_def)



#Generate map from names -> ids
ext_id_map = {}
for df in ext_defs:
    ext_id_map[df.name] = df.id

for df in ext_defs:
    print(df.serialize(pretty=True))

iot_infra_functions = ["Coordinator", "Router", "End Device"]
#Extension Class for IOT Devices
@stix2.v21.CustomObject(
        'iot-infrastrucutre', [
            ('name', stix2.properties.StringProperty(required=True)),
            ('description', stix2.properties.StringProperty(required=False)),
            ('infrastructure_function', stix2.properties.EnumProperty(allowed=iot_infra_functions, required=True)),
            ], extension_name=ext_id_map["iot-infrastrucutre"], is_sdo=True,
        )
class IOT_Device:
    pass

@stix2.v21.CustomObject(
        'zbee-nwk-addr', [
            ('name', stix2.properties.StringProperty(required=True)),
            ('value', stix2.properties.StringProperty(required=True)),
            ('resolves_to_refs', stix2.properties.ListProperty(stix2.properties.StringProperty, required=False)),
            ], extension_name=ext_id_map["zbee-nwk-addr"], is_sdo=True,
        )
class ZBee_NWK_Addr:
    pass


#Extension Class for IOT Traffic
@stix2.v21.CustomObject(
        'zigbee-traffic', [
            ('name', stix2.properties.StringProperty(required=True)),
            ('protocol', stix2.properties.StringProperty(required=True)),
            ('mac_src', stix2.properties.StringProperty(required=False)),
            ('mac_dst', stix2.properties.StringProperty(required=False)),
            ('nwk_src', stix2.properties.StringProperty(required=False)),
            ('nwk_dst', stix2.properties.StringProperty(required=False)),
            ('extended_source', stix2.properties.StringProperty(required=False)),
            ('src_64', stix2.properties.StringProperty(required=False)),
            ('mac_sn', stix2.properties.StringProperty(required=False)),
            ('nwk_sn', stix2.properties.StringProperty(required=False)),
            ('utc_date', stix2.properties.StringProperty(required=True)),
            ('length', stix2.properties.StringProperty(required=True)),
            ('device_addr', stix2.properties.StringProperty(required=False)),
            ('dest_plan', stix2.properties.StringProperty(required=False)),
            ('key', stix2.properties.StringProperty(required=False)),
            ('profile', stix2.properties.StringProperty(required=False)),
            ('zbee_aps_header', stix2.properties.StringProperty(required=False)),
            ('dst_endpt', stix2.properties.StringProperty(required=False)),
            ('cluster', stix2.properties.StringProperty(required=False)),
            ('src_endpt', stix2.properties.StringProperty(required=False)),
            ('counter', stix2.properties.StringProperty(required=False)),
            ('sec_ctrl_fld', stix2.properties.StringProperty(required=False)),
            ('frame_counter', stix2.properties.StringProperty(required=False)),
            ('ext_src', stix2.properties.StringProperty(required=False)),
            ('mic', stix2.properties.StringProperty(required=False)),
            ('key', stix2.properties.StringProperty(required=False)),
            ('key_label', stix2.properties.StringProperty(required=False)),
            ('zbee_cluster_lib', stix2.properties.StringProperty(required=False)),
            ('manufacturer_code', stix2.properties.StringProperty(required=False)),
            ('seq_num', stix2.properties.StringProperty(required=False)),
            ('command', stix2.properties.StringProperty(required=False)),
            ('respond_to_command', stix2.properties.StringProperty(required=False)),
            ('status', stix2.properties.StringProperty(required=False)),
            ('command_id', stix2.properties.StringProperty(required=False)),
            ('command_options', stix2.properties.StringProperty(required=False)),
            ('route_id', stix2.properties.StringProperty(required=False)),
            ('info', stix2.properties.StringProperty(required=True)),
        ], extension_name=ext_id_map["iot-traffic"], is_sdo=False,
    )
class Zigbee_Traffic:
    pass


#dev = Zigbee_Traffic(name="test", protocol="test2", utc_date="test3", length="1", info="test4")
#print(dev.serialize(pretty=True))






