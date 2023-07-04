from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FormsSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The isBingImageSearchEnabled property
    is_bing_image_search_enabled: Optional[bool] = None
    # The isExternalSendFormEnabled property
    is_external_send_form_enabled: Optional[bool] = None
    # The isExternalShareCollaborationEnabled property
    is_external_share_collaboration_enabled: Optional[bool] = None
    # The isExternalShareResultEnabled property
    is_external_share_result_enabled: Optional[bool] = None
    # The isExternalShareTemplateEnabled property
    is_external_share_template_enabled: Optional[bool] = None
    # The isInOrgFormsPhishingScanEnabled property
    is_in_org_forms_phishing_scan_enabled: Optional[bool] = None
    # The isRecordIdentityByDefaultEnabled property
    is_record_identity_by_default_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FormsSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FormsSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FormsSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isBingImageSearchEnabled": lambda n : setattr(self, 'is_bing_image_search_enabled', n.get_bool_value()),
            "isExternalSendFormEnabled": lambda n : setattr(self, 'is_external_send_form_enabled', n.get_bool_value()),
            "isExternalShareCollaborationEnabled": lambda n : setattr(self, 'is_external_share_collaboration_enabled', n.get_bool_value()),
            "isExternalShareResultEnabled": lambda n : setattr(self, 'is_external_share_result_enabled', n.get_bool_value()),
            "isExternalShareTemplateEnabled": lambda n : setattr(self, 'is_external_share_template_enabled', n.get_bool_value()),
            "isInOrgFormsPhishingScanEnabled": lambda n : setattr(self, 'is_in_org_forms_phishing_scan_enabled', n.get_bool_value()),
            "isRecordIdentityByDefaultEnabled": lambda n : setattr(self, 'is_record_identity_by_default_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("isBingImageSearchEnabled", self.is_bing_image_search_enabled)
        writer.write_bool_value("isExternalSendFormEnabled", self.is_external_send_form_enabled)
        writer.write_bool_value("isExternalShareCollaborationEnabled", self.is_external_share_collaboration_enabled)
        writer.write_bool_value("isExternalShareResultEnabled", self.is_external_share_result_enabled)
        writer.write_bool_value("isExternalShareTemplateEnabled", self.is_external_share_template_enabled)
        writer.write_bool_value("isInOrgFormsPhishingScanEnabled", self.is_in_org_forms_phishing_scan_enabled)
        writer.write_bool_value("isRecordIdentityByDefaultEnabled", self.is_record_identity_by_default_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

