from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ApproveAppsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the approveApps method.
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
    def approve_all_permissions(self,) -> Optional[bool]:
        """
        Gets the approveAllPermissions property value. The approveAllPermissions property
        Returns: Optional[bool]
        """
        return self._approve_all_permissions
    
    @approve_all_permissions.setter
    def approve_all_permissions(self,value: Optional[bool] = None) -> None:
        """
        Sets the approveAllPermissions property value. The approveAllPermissions property
        Args:
            value: Value to set for the approveAllPermissions property.
        """
        self._approve_all_permissions = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new approveAppsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The approveAllPermissions property
        self._approve_all_permissions: Optional[bool] = None
        # The packageIds property
        self._package_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApproveAppsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApproveAppsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApproveAppsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "approve_all_permissions": lambda n : setattr(self, 'approve_all_permissions', n.get_bool_value()),
            "package_ids": lambda n : setattr(self, 'package_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def package_ids(self,) -> Optional[List[str]]:
        """
        Gets the packageIds property value. The packageIds property
        Returns: Optional[List[str]]
        """
        return self._package_ids
    
    @package_ids.setter
    def package_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the packageIds property value. The packageIds property
        Args:
            value: Value to set for the packageIds property.
        """
        self._package_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("approveAllPermissions", self.approve_all_permissions)
        writer.write_collection_of_primitive_values("packageIds", self.package_ids)
        writer.write_additional_data_value(self.additional_data)
    

