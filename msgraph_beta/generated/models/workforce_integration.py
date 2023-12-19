from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .workforce_integration_eligibility_filtering_enabled_entities import WorkforceIntegration_eligibilityFilteringEnabledEntities
    from .workforce_integration_encryption import WorkforceIntegrationEncryption
    from .workforce_integration_supported_entities import WorkforceIntegration_supportedEntities
    from .workforce_integration_supports import WorkforceIntegration_supports

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class WorkforceIntegration(ChangeTrackedEntity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.workforceIntegration"
    # API version for the callback URL. Start with 1.
    api_version: Optional[int] = None
    # Name of the workforce integration.
    display_name: Optional[str] = None
    # The eligibilityFilteringEnabledEntities property
    eligibility_filtering_enabled_entities: Optional[WorkforceIntegration_eligibilityFilteringEnabledEntities] = None
    # The workforce integration encryption resource.
    encryption: Optional[WorkforceIntegrationEncryption] = None
    # Indicates whether this workforce integration is currently active and available.
    is_active: Optional[bool] = None
    # This property has replaced supports in v1.0. We recommend that you use this property instead of supports. The supports property is still supported in beta for the time being. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. You must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
    supported_entities: Optional[WorkforceIntegration_supportedEntities] = None
    # The Shifts entities supported for synchronous change notifications. Shifts make a callback to the url provided on client changes on those entities added here. By default, no entities are supported for change notifications. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. You must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
    supports: Optional[WorkforceIntegration_supports] = None
    # Workforce Integration URL for callbacks from the Shifts service.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkforceIntegration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkforceIntegration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkforceIntegration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .workforce_integration_eligibility_filtering_enabled_entities import WorkforceIntegration_eligibilityFilteringEnabledEntities
        from .workforce_integration_encryption import WorkforceIntegrationEncryption
        from .workforce_integration_supported_entities import WorkforceIntegration_supportedEntities
        from .workforce_integration_supports import WorkforceIntegration_supports

        from .change_tracked_entity import ChangeTrackedEntity
        from .workforce_integration_eligibility_filtering_enabled_entities import WorkforceIntegration_eligibilityFilteringEnabledEntities
        from .workforce_integration_encryption import WorkforceIntegrationEncryption
        from .workforce_integration_supported_entities import WorkforceIntegration_supportedEntities
        from .workforce_integration_supports import WorkforceIntegration_supports

        fields: Dict[str, Callable[[Any], None]] = {
            "apiVersion": lambda n : setattr(self, 'api_version', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "eligibilityFilteringEnabledEntities": lambda n : setattr(self, 'eligibility_filtering_enabled_entities', n.get_enum_value(WorkforceIntegration_eligibilityFilteringEnabledEntities)),
            "encryption": lambda n : setattr(self, 'encryption', n.get_object_value(WorkforceIntegrationEncryption)),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "supportedEntities": lambda n : setattr(self, 'supported_entities', n.get_enum_value(WorkforceIntegration_supportedEntities)),
            "supports": lambda n : setattr(self, 'supports', n.get_enum_value(WorkforceIntegration_supports)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("apiVersion", self.api_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("eligibilityFilteringEnabledEntities", self.eligibility_filtering_enabled_entities)
        writer.write_object_value("encryption", self.encryption)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_enum_value("supportedEntities", self.supported_entities)
        writer.write_enum_value("supports", self.supports)
        writer.write_str_value("url", self.url)
    

