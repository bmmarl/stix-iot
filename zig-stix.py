from stix2 import Bundle, parse, ExtensionDefinition
import stix2
import json
import uuid
from uuid import uuid5

SCO_DET_ID_NAMESPACE = uuid.UUID('00abedb4-aa42-466c-9c01-fed23315a9b7')
def gen_uuid(string):
    return f'{string}--{uuid.uuid5(SCO_DET_ID_NAMESPACE,string)}'

#TODO Create Extensions for IOT Traffic and Devices

iot_device_def = ExtensionDefinition(
        id=gen_uuid("extension-definition"),
        created_by_ref=gen_uuid("identity"),
        name="iot-infrastrucutre",
        description="This extension creates a new SDO that can be used to represent IoT devices, sensors, hubs, etc.",
        schema="https://raw.githubusercontent.com/bmmarl/stix-iot/refs/heads/main/STIG/src/static/jsedit/iot-infrastructure.json",
        version="1.0",
        extension_types=[
    	    "new-sdo"
        ])

iot_traffic_def = ExtensionDefinition(
        id=gen_uuid("extension-definition"),
        created_by_ref=gen_uuid("identity"),
        name="iot-traffic",
        description="This extension creates a new SCO that can be used to represent traffic between IoT Devices, specifically under the IEEE 803.15.4 standard and ZigBee protcol.",
        schema="",
        version="1.0",
        extension_types=[
            "new-sco"
        ])



#print(iot_device_def.serialize(pretty=True))

#Extension Class for IOT Devices
@stix2.v21.CustomObject(
        'iot-device', [
            ('name', stix2.properties.StringProperty(required=True)),
            ('zigbee_network_address', stix2.properties.StringProperty(required=True)),
            ('ieee_802_15_4_mac_address', stix2.properties.StringProperty(required=True)),
            ], extension_name=ext_id_map["IOT Device"], is_sdo=True,
        )
class IOT_Device:
    pass

#Extension Class for IOT Traffic
@stix2.v21.CustomObject(
        'zigbee_traffic', [
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
        ], extension_name=ext_id_map["IEEE 802.15.4 Traffic"], is_sdo=False,
    )
class Zigbee_Traffic:
    pass










