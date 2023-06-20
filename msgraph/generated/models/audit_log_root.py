from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_audit, provisioning_object_summary, sign_in

@dataclass
class AuditLogRoot(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The directoryAudits property
    directory_audits: Optional[List[directory_audit.DirectoryAudit]] = None
    # The directoryProvisioning property
    directory_provisioning: Optional[List[provisioning_object_summary.ProvisioningObjectSummary]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provisioning property
    provisioning: Optional[List[provisioning_object_summary.ProvisioningObjectSummary]] = None
    # The signIns property
    sign_ins: Optional[List[sign_in.SignIn]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditLogRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuditLogRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_audit, provisioning_object_summary, sign_in

        from . import directory_audit, provisioning_object_summary, sign_in

        fields: Dict[str, Callable[[Any], None]] = {
            "directoryAudits": lambda n : setattr(self, 'directory_audits', n.get_collection_of_object_values(directory_audit.DirectoryAudit)),
            "directoryProvisioning": lambda n : setattr(self, 'directory_provisioning', n.get_collection_of_object_values(provisioning_object_summary.ProvisioningObjectSummary)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioning": lambda n : setattr(self, 'provisioning', n.get_collection_of_object_values(provisioning_object_summary.ProvisioningObjectSummary)),
            "signIns": lambda n : setattr(self, 'sign_ins', n.get_collection_of_object_values(sign_in.SignIn)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("directoryAudits", self.directory_audits)
        writer.write_collection_of_object_values("directoryProvisioning", self.directory_provisioning)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("provisioning", self.provisioning)
        writer.write_collection_of_object_values("signIns", self.sign_ins)
        writer.write_additional_data_value(self.additional_data)
    

