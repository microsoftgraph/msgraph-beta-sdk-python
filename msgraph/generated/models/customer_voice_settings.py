from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerVoiceSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Controls whether phishing protection is run on forms created by users, blocking the creation of forms if common phishing questions are detected.
    is_in_org_forms_phishing_scan_enabled: Optional[bool] = None
    # Controls whether the names of users who fill out forms are recorded.
    is_record_identity_by_default_enabled: Optional[bool] = None
    # Controls whether only users inside your organization can submit a response.
    is_restricted_survey_access_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomerVoiceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerVoiceSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomerVoiceSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isInOrgFormsPhishingScanEnabled": lambda n : setattr(self, 'is_in_org_forms_phishing_scan_enabled', n.get_bool_value()),
            "isRecordIdentityByDefaultEnabled": lambda n : setattr(self, 'is_record_identity_by_default_enabled', n.get_bool_value()),
            "isRestrictedSurveyAccessEnabled": lambda n : setattr(self, 'is_restricted_survey_access_enabled', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isInOrgFormsPhishingScanEnabled", self.is_in_org_forms_phishing_scan_enabled)
        writer.write_bool_value("isRecordIdentityByDefaultEnabled", self.is_record_identity_by_default_enabled)
        writer.write_bool_value("isRestrictedSurveyAccessEnabled", self.is_restricted_survey_access_enabled)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

