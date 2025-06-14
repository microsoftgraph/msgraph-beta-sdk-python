from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detonation_details import DetonationDetails
    from .threat_type import ThreatType

@dataclass
class AnalyzedEmailAttachment(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The detonation details of the attachment.
    detonation_details: Optional[DetonationDetails] = None
    # Extension of the file.
    file_extension: Optional[str] = None
    # The name of the attachment in the email.
    file_name: Optional[str] = None
    # Size of the file.
    file_size: Optional[int] = None
    # The type of the attachment in the email.
    file_type: Optional[str] = None
    # The threat name associated with the threat type.
    malware_family: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The SHA256 file hash of the attachment.
    sha256: Optional[str] = None
    # Details of entries in tenant allow/block list configured by tenant.
    tenant_allow_block_list_detail_info: Optional[str] = None
    # The threat type associated with the attachment. The possible values are: unknown, spam, malware, phishing, none, unknownFutureValue.
    threat_type: Optional[ThreatType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyzedEmailAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmailAttachment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmailAttachment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .detonation_details import DetonationDetails
        from .threat_type import ThreatType

        from .detonation_details import DetonationDetails
        from .threat_type import ThreatType

        fields: dict[str, Callable[[Any], None]] = {
            "detonationDetails": lambda n : setattr(self, 'detonation_details', n.get_object_value(DetonationDetails)),
            "fileExtension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "malwareFamily": lambda n : setattr(self, 'malware_family', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sha256": lambda n : setattr(self, 'sha256', n.get_str_value()),
            "tenantAllowBlockListDetailInfo": lambda n : setattr(self, 'tenant_allow_block_list_detail_info', n.get_str_value()),
            "threatType": lambda n : setattr(self, 'threat_type', n.get_enum_value(ThreatType)),
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
        writer.write_object_value("detonationDetails", self.detonation_details)
        writer.write_str_value("fileExtension", self.file_extension)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("fileType", self.file_type)
        writer.write_str_value("malwareFamily", self.malware_family)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sha256", self.sha256)
        writer.write_str_value("tenantAllowBlockListDetailInfo", self.tenant_allow_block_list_detail_info)
        writer.write_enum_value("threatType", self.threat_type)
        writer.write_additional_data_value(self.additional_data)
    

