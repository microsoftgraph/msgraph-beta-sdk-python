from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dh_group, ike_encryption, ike_integrity, ip_sec_encryption, ip_sec_integrity, pfs_group, tunnel_configuration

from . import tunnel_configuration

@dataclass
class TunnelConfigurationIKEv2Custom(tunnel_configuration.TunnelConfiguration):
    odata_type = "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Custom"
    # The dhGroup property
    dh_group: Optional[dh_group.DhGroup] = None
    # The ikeEncryption property
    ike_encryption: Optional[ike_encryption.IkeEncryption] = None
    # The ikeIntegrity property
    ike_integrity: Optional[ike_integrity.IkeIntegrity] = None
    # The ipSecEncryption property
    ip_sec_encryption: Optional[ip_sec_encryption.IpSecEncryption] = None
    # The ipSecIntegrity property
    ip_sec_integrity: Optional[ip_sec_integrity.IpSecIntegrity] = None
    # The pfsGroup property
    pfs_group: Optional[pfs_group.PfsGroup] = None
    # The saLifeTimeSeconds property
    sa_life_time_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TunnelConfigurationIKEv2Custom:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TunnelConfigurationIKEv2Custom
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TunnelConfigurationIKEv2Custom()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import dh_group, ike_encryption, ike_integrity, ip_sec_encryption, ip_sec_integrity, pfs_group, tunnel_configuration

        from . import dh_group, ike_encryption, ike_integrity, ip_sec_encryption, ip_sec_integrity, pfs_group, tunnel_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "dhGroup": lambda n : setattr(self, 'dh_group', n.get_enum_value(dh_group.DhGroup)),
            "ikeEncryption": lambda n : setattr(self, 'ike_encryption', n.get_enum_value(ike_encryption.IkeEncryption)),
            "ikeIntegrity": lambda n : setattr(self, 'ike_integrity', n.get_enum_value(ike_integrity.IkeIntegrity)),
            "ipSecEncryption": lambda n : setattr(self, 'ip_sec_encryption', n.get_enum_value(ip_sec_encryption.IpSecEncryption)),
            "ipSecIntegrity": lambda n : setattr(self, 'ip_sec_integrity', n.get_enum_value(ip_sec_integrity.IpSecIntegrity)),
            "pfsGroup": lambda n : setattr(self, 'pfs_group', n.get_enum_value(pfs_group.PfsGroup)),
            "saLifeTimeSeconds": lambda n : setattr(self, 'sa_life_time_seconds', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("dhGroup", self.dh_group)
        writer.write_enum_value("ikeEncryption", self.ike_encryption)
        writer.write_enum_value("ikeIntegrity", self.ike_integrity)
        writer.write_enum_value("ipSecEncryption", self.ip_sec_encryption)
        writer.write_enum_value("ipSecIntegrity", self.ip_sec_integrity)
        writer.write_enum_value("pfsGroup", self.pfs_group)
        writer.write_int_value("saLifeTimeSeconds", self.sa_life_time_seconds)
    

