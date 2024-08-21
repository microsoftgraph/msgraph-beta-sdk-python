from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_security_attribute_audit import CustomSecurityAttributeAudit
    from .directory_audit import DirectoryAudit
    from .provisioning_object_summary import ProvisioningObjectSummary
    from .sign_in import SignIn

@dataclass
class AuditLogRoot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents a custom security attribute audit log.
    custom_security_attribute_audits: Optional[List[CustomSecurityAttributeAudit]] = None
    # The directoryAudits property
    directory_audits: Optional[List[DirectoryAudit]] = None
    # The directoryProvisioning property
    directory_provisioning: Optional[List[ProvisioningObjectSummary]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents an action performed by the Microsoft Entra provisioning service and its associated properties.
    provisioning: Optional[List[ProvisioningObjectSummary]] = None
    # The signIns property
    sign_ins: Optional[List[SignIn]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditLogRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditLogRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_security_attribute_audit import CustomSecurityAttributeAudit
        from .directory_audit import DirectoryAudit
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .sign_in import SignIn

        from .custom_security_attribute_audit import CustomSecurityAttributeAudit
        from .directory_audit import DirectoryAudit
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .sign_in import SignIn

        fields: Dict[str, Callable[[Any], None]] = {
            "customSecurityAttributeAudits": lambda n : setattr(self, 'custom_security_attribute_audits', n.get_collection_of_object_values(CustomSecurityAttributeAudit)),
            "directoryAudits": lambda n : setattr(self, 'directory_audits', n.get_collection_of_object_values(DirectoryAudit)),
            "directoryProvisioning": lambda n : setattr(self, 'directory_provisioning', n.get_collection_of_object_values(ProvisioningObjectSummary)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioning": lambda n : setattr(self, 'provisioning', n.get_collection_of_object_values(ProvisioningObjectSummary)),
            "signIns": lambda n : setattr(self, 'sign_ins', n.get_collection_of_object_values(SignIn)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("customSecurityAttributeAudits", self.custom_security_attribute_audits)
        writer.write_collection_of_object_values("directoryAudits", self.directory_audits)
        writer.write_collection_of_object_values("directoryProvisioning", self.directory_provisioning)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("provisioning", self.provisioning)
        writer.write_collection_of_object_values("signIns", self.sign_ins)
        writer.write_additional_data_value(self.additional_data)
    

