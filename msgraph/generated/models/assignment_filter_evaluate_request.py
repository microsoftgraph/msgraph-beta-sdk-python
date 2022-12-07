from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_platform_type = lazy_import('msgraph.generated.models.device_platform_type')

class AssignmentFilterEvaluateRequest(AdditionalDataHolder, Parsable):
    """
    Request for assignment filter evaluation for devices.
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
        Instantiates a new assignmentFilterEvaluateRequest and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Order the devices should be sorted in. Default is ascending on device name.
        self._order_by: Optional[List[str]] = None
        # Supported platform types.
        self._platform: Optional[device_platform_type.DevicePlatformType] = None
        # Rule definition of the Assignment Filter.
        self._rule: Optional[str] = None
        # Search keyword applied to scope found devices.
        self._search: Optional[str] = None
        # Number of records to skip. Default value is 0
        self._skip: Optional[int] = None
        # Limit of records per request. Default value is 100, if provided less than 0 or greater than 100
        self._top: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentFilterEvaluateRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterEvaluateRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignmentFilterEvaluateRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "order_by": lambda n : setattr(self, 'order_by', n.get_collection_of_primitive_values(str)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "rule": lambda n : setattr(self, 'rule', n.get_str_value()),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "skip": lambda n : setattr(self, 'skip', n.get_int_value()),
            "top": lambda n : setattr(self, 'top', n.get_int_value()),
        }
        return fields
    
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
    
    @property
    def order_by(self,) -> Optional[List[str]]:
        """
        Gets the orderBy property value. Order the devices should be sorted in. Default is ascending on device name.
        Returns: Optional[List[str]]
        """
        return self._order_by
    
    @order_by.setter
    def order_by(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the orderBy property value. Order the devices should be sorted in. Default is ascending on device name.
        Args:
            value: Value to set for the orderBy property.
        """
        self._order_by = value
    
    @property
    def platform(self,) -> Optional[device_platform_type.DevicePlatformType]:
        """
        Gets the platform property value. Supported platform types.
        Returns: Optional[device_platform_type.DevicePlatformType]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[device_platform_type.DevicePlatformType] = None) -> None:
        """
        Sets the platform property value. Supported platform types.
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def rule(self,) -> Optional[str]:
        """
        Gets the rule property value. Rule definition of the Assignment Filter.
        Returns: Optional[str]
        """
        return self._rule
    
    @rule.setter
    def rule(self,value: Optional[str] = None) -> None:
        """
        Sets the rule property value. Rule definition of the Assignment Filter.
        Args:
            value: Value to set for the rule property.
        """
        self._rule = value
    
    @property
    def search(self,) -> Optional[str]:
        """
        Gets the search property value. Search keyword applied to scope found devices.
        Returns: Optional[str]
        """
        return self._search
    
    @search.setter
    def search(self,value: Optional[str] = None) -> None:
        """
        Sets the search property value. Search keyword applied to scope found devices.
        Args:
            value: Value to set for the search property.
        """
        self._search = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("orderBy", self.order_by)
        writer.write_enum_value("platform", self.platform)
        writer.write_str_value("rule", self.rule)
        writer.write_str_value("search", self.search)
        writer.write_int_value("skip", self.skip)
        writer.write_int_value("top", self.top)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def skip(self,) -> Optional[int]:
        """
        Gets the skip property value. Number of records to skip. Default value is 0
        Returns: Optional[int]
        """
        return self._skip
    
    @skip.setter
    def skip(self,value: Optional[int] = None) -> None:
        """
        Sets the skip property value. Number of records to skip. Default value is 0
        Args:
            value: Value to set for the skip property.
        """
        self._skip = value
    
    @property
    def top(self,) -> Optional[int]:
        """
        Gets the top property value. Limit of records per request. Default value is 100, if provided less than 0 or greater than 100
        Returns: Optional[int]
        """
        return self._top
    
    @top.setter
    def top(self,value: Optional[int] = None) -> None:
        """
        Sets the top property value. Limit of records per request. Default value is 100, if provided less than 0 or greater than 100
        Args:
            value: Value to set for the top property.
        """
        self._top = value
    

