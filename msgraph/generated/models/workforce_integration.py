from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')
eligibility_filtering_enabled_entities = lazy_import('msgraph.generated.models.eligibility_filtering_enabled_entities')
workforce_integration_encryption = lazy_import('msgraph.generated.models.workforce_integration_encryption')
workforce_integration_supported_entities = lazy_import('msgraph.generated.models.workforce_integration_supported_entities')

class WorkforceIntegration(change_tracked_entity.ChangeTrackedEntity):
    @property
    def api_version(self,) -> Optional[int]:
        """
        Gets the apiVersion property value. API version for the call back URL. Start with 1.
        Returns: Optional[int]
        """
        return self._api_version
    
    @api_version.setter
    def api_version(self,value: Optional[int] = None) -> None:
        """
        Sets the apiVersion property value. API version for the call back URL. Start with 1.
        Args:
            value: Value to set for the apiVersion property.
        """
        self._api_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WorkforceIntegration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.workforceIntegration"
        # API version for the call back URL. Start with 1.
        self._api_version: Optional[int] = None
        # Name of the workforce integration.
        self._display_name: Optional[str] = None
        # The eligibilityFilteringEnabledEntities property
        self._eligibility_filtering_enabled_entities: Optional[eligibility_filtering_enabled_entities.EligibilityFilteringEnabledEntities] = None
        # The workforce integration encryption resource.
        self._encryption: Optional[workforce_integration_encryption.WorkforceIntegrationEncryption] = None
        # Indicates whether this workforce integration is currently active and available.
        self._is_active: Optional[bool] = None
        # This property has replaced supports in v1.0. We recommend that you use this property instead of supports. The supports property is still supported in beta for the time being. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
        self._supported_entities: Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities] = None
        # The Shifts entities supported for synchronous change notifications. Shifts will make a call back to the url provided on client changes on those entities added here. By default, no entities are supported for change notifications. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
        self._supports: Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities] = None
        # Workforce Integration URL for callbacks from the Shifts service.
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkforceIntegration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkforceIntegration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkforceIntegration()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the workforce integration.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the workforce integration.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def eligibility_filtering_enabled_entities(self,) -> Optional[eligibility_filtering_enabled_entities.EligibilityFilteringEnabledEntities]:
        """
        Gets the eligibilityFilteringEnabledEntities property value. The eligibilityFilteringEnabledEntities property
        Returns: Optional[eligibility_filtering_enabled_entities.EligibilityFilteringEnabledEntities]
        """
        return self._eligibility_filtering_enabled_entities
    
    @eligibility_filtering_enabled_entities.setter
    def eligibility_filtering_enabled_entities(self,value: Optional[eligibility_filtering_enabled_entities.EligibilityFilteringEnabledEntities] = None) -> None:
        """
        Sets the eligibilityFilteringEnabledEntities property value. The eligibilityFilteringEnabledEntities property
        Args:
            value: Value to set for the eligibilityFilteringEnabledEntities property.
        """
        self._eligibility_filtering_enabled_entities = value
    
    @property
    def encryption(self,) -> Optional[workforce_integration_encryption.WorkforceIntegrationEncryption]:
        """
        Gets the encryption property value. The workforce integration encryption resource.
        Returns: Optional[workforce_integration_encryption.WorkforceIntegrationEncryption]
        """
        return self._encryption
    
    @encryption.setter
    def encryption(self,value: Optional[workforce_integration_encryption.WorkforceIntegrationEncryption] = None) -> None:
        """
        Sets the encryption property value. The workforce integration encryption resource.
        Args:
            value: Value to set for the encryption property.
        """
        self._encryption = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "api_version": lambda n : setattr(self, 'api_version', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "eligibility_filtering_enabled_entities": lambda n : setattr(self, 'eligibility_filtering_enabled_entities', n.get_enum_value(eligibility_filtering_enabled_entities.EligibilityFilteringEnabledEntities)),
            "encryption": lambda n : setattr(self, 'encryption', n.get_object_value(workforce_integration_encryption.WorkforceIntegrationEncryption)),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "supported_entities": lambda n : setattr(self, 'supported_entities', n.get_enum_value(workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities)),
            "supports": lambda n : setattr(self, 'supports', n.get_enum_value(workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether this workforce integration is currently active and available.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether this workforce integration is currently active and available.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("apiVersion", self.api_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("eligibilityFilteringEnabledEntities", self.eligibility_filtering_enabled_entities)
        writer.write_object_value("encryption", self.encryption)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_enum_value("supportedEntities", self.supported_entities)
        writer.write_enum_value("supports", self.supports)
        writer.write_str_value("url", self.url)
    
    @property
    def supported_entities(self,) -> Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities]:
        """
        Gets the supportedEntities property value. This property has replaced supports in v1.0. We recommend that you use this property instead of supports. The supports property is still supported in beta for the time being. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
        Returns: Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities]
        """
        return self._supported_entities
    
    @supported_entities.setter
    def supported_entities(self,value: Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities] = None) -> None:
        """
        Sets the supportedEntities property value. This property has replaced supports in v1.0. We recommend that you use this property instead of supports. The supports property is still supported in beta for the time being. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
        Args:
            value: Value to set for the supportedEntities property.
        """
        self._supported_entities = value
    
    @property
    def supports(self,) -> Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities]:
        """
        Gets the supports property value. The Shifts entities supported for synchronous change notifications. Shifts will make a call back to the url provided on client changes on those entities added here. By default, no entities are supported for change notifications. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
        Returns: Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities]
        """
        return self._supports
    
    @supports.setter
    def supports(self,value: Optional[workforce_integration_supported_entities.WorkforceIntegrationSupportedEntities] = None) -> None:
        """
        Sets the supports property value. The Shifts entities supported for synchronous change notifications. Shifts will make a call back to the url provided on client changes on those entities added here. By default, no entities are supported for change notifications. The possible values are: none, shift, swapRequest, openshift, openShiftRequest, userShiftPreferences, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard, timeOffReason, timeOff, timeOffRequest. If selecting more than one value, all values must start with the first letter in uppercase.
        Args:
            value: Value to set for the supports property.
        """
        self._supports = value
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. Workforce Integration URL for callbacks from the Shifts service.
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. Workforce Integration URL for callbacks from the Shifts service.
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

