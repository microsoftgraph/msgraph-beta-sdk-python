from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
feature_type = lazy_import('msgraph.generated.models.feature_type')
usage_auth_method = lazy_import('msgraph.generated.models.usage_auth_method')

class CredentialUsageSummary(entity.Entity):
    @property
    def auth_method(self,) -> Optional[usage_auth_method.UsageAuthMethod]:
        """
        Gets the authMethod property value. The authMethod property
        Returns: Optional[usage_auth_method.UsageAuthMethod]
        """
        return self._auth_method
    
    @auth_method.setter
    def auth_method(self,value: Optional[usage_auth_method.UsageAuthMethod] = None) -> None:
        """
        Sets the authMethod property value. The authMethod property
        Args:
            value: Value to set for the authMethod property.
        """
        self._auth_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CredentialUsageSummary and sets the default values.
        """
        super().__init__()
        # The authMethod property
        self._auth_method: Optional[usage_auth_method.UsageAuthMethod] = None
        # Provides the count of failed resets or registration data.
        self._failure_activity_count: Optional[int] = None
        # The feature property
        self._feature: Optional[feature_type.FeatureType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Provides the count of successful registrations or resets.
        self._successful_activity_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialUsageSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUsageSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CredentialUsageSummary()
    
    @property
    def failure_activity_count(self,) -> Optional[int]:
        """
        Gets the failureActivityCount property value. Provides the count of failed resets or registration data.
        Returns: Optional[int]
        """
        return self._failure_activity_count
    
    @failure_activity_count.setter
    def failure_activity_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failureActivityCount property value. Provides the count of failed resets or registration data.
        Args:
            value: Value to set for the failureActivityCount property.
        """
        self._failure_activity_count = value
    
    @property
    def feature(self,) -> Optional[feature_type.FeatureType]:
        """
        Gets the feature property value. The feature property
        Returns: Optional[feature_type.FeatureType]
        """
        return self._feature
    
    @feature.setter
    def feature(self,value: Optional[feature_type.FeatureType] = None) -> None:
        """
        Sets the feature property value. The feature property
        Args:
            value: Value to set for the feature property.
        """
        self._feature = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "auth_method": lambda n : setattr(self, 'auth_method', n.get_enum_value(usage_auth_method.UsageAuthMethod)),
            "failure_activity_count": lambda n : setattr(self, 'failure_activity_count', n.get_int_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(feature_type.FeatureType)),
            "successful_activity_count": lambda n : setattr(self, 'successful_activity_count', n.get_int_value()),
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
        writer.write_enum_value("authMethod", self.auth_method)
        writer.write_int_value("failureActivityCount", self.failure_activity_count)
        writer.write_enum_value("feature", self.feature)
        writer.write_int_value("successfulActivityCount", self.successful_activity_count)
    
    @property
    def successful_activity_count(self,) -> Optional[int]:
        """
        Gets the successfulActivityCount property value. Provides the count of successful registrations or resets.
        Returns: Optional[int]
        """
        return self._successful_activity_count
    
    @successful_activity_count.setter
    def successful_activity_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulActivityCount property value. Provides the count of successful registrations or resets.
        Args:
            value: Value to set for the successfulActivityCount property.
        """
        self._successful_activity_count = value
    

