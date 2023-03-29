from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import host, hostname, host_component, host_cookie, host_tracker, ip_address, passive_dns_record, unclassified_artifact
    from .. import entity

from .. import entity

class Artifact(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new artifact and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Artifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Artifact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.security.host":
                from . import host

                return host.Host()
            if mapping_value == "#microsoft.graph.security.hostComponent":
                from . import host_component

                return host_component.HostComponent()
            if mapping_value == "#microsoft.graph.security.hostCookie":
                from . import host_cookie

                return host_cookie.HostCookie()
            if mapping_value == "#microsoft.graph.security.hostname":
                from . import hostname

                return hostname.Hostname()
            if mapping_value == "#microsoft.graph.security.hostTracker":
                from . import host_tracker

                return host_tracker.HostTracker()
            if mapping_value == "#microsoft.graph.security.ipAddress":
                from . import ip_address

                return ip_address.IpAddress()
            if mapping_value == "#microsoft.graph.security.passiveDnsRecord":
                from . import passive_dns_record

                return passive_dns_record.PassiveDnsRecord()
            if mapping_value == "#microsoft.graph.security.unclassifiedArtifact":
                from . import unclassified_artifact

                return unclassified_artifact.UnclassifiedArtifact()
        return Artifact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import host, hostname, host_component, host_cookie, host_tracker, ip_address, passive_dns_record, unclassified_artifact
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

