from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserExperienceAnalyticsDeviceScopeSummary(AdditionalDataHolder, Parsable):
    """
    The user experience analytics tenant level information for all the device scope configurations
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def completed_device_scope_ids(self,) -> Optional[List[str]]:
        """
        Gets the completedDeviceScopeIds property value. A collection of the user experience analytics device scope Unique Identifiers that are enabled and finished recalculating the report metric.
        Returns: Optional[List[str]]
        """
        return self._completed_device_scope_ids
    
    @completed_device_scope_ids.setter
    def completed_device_scope_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the completedDeviceScopeIds property value. A collection of the user experience analytics device scope Unique Identifiers that are enabled and finished recalculating the report metric.
        Args:
            value: Value to set for the completedDeviceScopeIds property.
        """
        self._completed_device_scope_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsDeviceScopeSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A collection of the user experience analytics device scope Unique Identifiers that are enabled and finished recalculating the report metric.
        self._completed_device_scope_ids: Optional[List[str]] = None
        # A collection of user experience analytics device scope Unique Identitfiers that are enabled but there is insufficient data to calculate results.
        self._insufficient_data_device_scope_ids: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The total number of user experience analytics device scopes. Valid values -2147483648 to 2147483647
        self._total_device_scopes: Optional[int] = None
        # The total number of user experience analytics device scopes that are enabled. Valid values -2147483648 to 2147483647
        self._total_device_scopes_enabled: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceScopeSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceScopeSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceScopeSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_device_scope_ids": lambda n : setattr(self, 'completed_device_scope_ids', n.get_collection_of_primitive_values(str)),
            "insufficient_data_device_scope_ids": lambda n : setattr(self, 'insufficient_data_device_scope_ids', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total_device_scopes": lambda n : setattr(self, 'total_device_scopes', n.get_int_value()),
            "total_device_scopes_enabled": lambda n : setattr(self, 'total_device_scopes_enabled', n.get_int_value()),
        }
        return fields
    
    @property
    def insufficient_data_device_scope_ids(self,) -> Optional[List[str]]:
        """
        Gets the insufficientDataDeviceScopeIds property value. A collection of user experience analytics device scope Unique Identitfiers that are enabled but there is insufficient data to calculate results.
        Returns: Optional[List[str]]
        """
        return self._insufficient_data_device_scope_ids
    
    @insufficient_data_device_scope_ids.setter
    def insufficient_data_device_scope_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the insufficientDataDeviceScopeIds property value. A collection of user experience analytics device scope Unique Identitfiers that are enabled but there is insufficient data to calculate results.
        Args:
            value: Value to set for the insufficientDataDeviceScopeIds property.
        """
        self._insufficient_data_device_scope_ids = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("completedDeviceScopeIds", self.completed_device_scope_ids)
        writer.write_collection_of_primitive_values("insufficientDataDeviceScopeIds", self.insufficient_data_device_scope_ids)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalDeviceScopes", self.total_device_scopes)
        writer.write_int_value("totalDeviceScopesEnabled", self.total_device_scopes_enabled)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_device_scopes(self,) -> Optional[int]:
        """
        Gets the totalDeviceScopes property value. The total number of user experience analytics device scopes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._total_device_scopes
    
    @total_device_scopes.setter
    def total_device_scopes(self,value: Optional[int] = None) -> None:
        """
        Sets the totalDeviceScopes property value. The total number of user experience analytics device scopes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the totalDeviceScopes property.
        """
        self._total_device_scopes = value
    
    @property
    def total_device_scopes_enabled(self,) -> Optional[int]:
        """
        Gets the totalDeviceScopesEnabled property value. The total number of user experience analytics device scopes that are enabled. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._total_device_scopes_enabled
    
    @total_device_scopes_enabled.setter
    def total_device_scopes_enabled(self,value: Optional[int] = None) -> None:
        """
        Sets the totalDeviceScopesEnabled property value. The total number of user experience analytics device scopes that are enabled. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the totalDeviceScopesEnabled property.
        """
        self._total_device_scopes_enabled = value
    

