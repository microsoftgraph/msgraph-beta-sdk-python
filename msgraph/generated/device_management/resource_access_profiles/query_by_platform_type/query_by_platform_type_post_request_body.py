from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_platform_type = lazy_import('msgraph.generated.models.policy_platform_type')

class QueryByPlatformTypePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the queryByPlatformType method.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new queryByPlatformTypePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Supported platform types for policies.
        self._platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> QueryByPlatformTypePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: QueryByPlatformTypePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return QueryByPlatformTypePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
        }
        return fields
    
    @property
    def platform_type(self,) -> Optional[policy_platform_type.PolicyPlatformType]:
        """
        Gets the platformType property value. Supported platform types for policies.
        Returns: Optional[policy_platform_type.PolicyPlatformType]
        """
        return self._platform_type
    
    @platform_type.setter
    def platform_type(self,value: Optional[policy_platform_type.PolicyPlatformType] = None) -> None:
        """
        Sets the platformType property value. Supported platform types for policies.
        Args:
            value: Value to set for the platformType property.
        """
        self._platform_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_additional_data_value(self.additional_data)
    

