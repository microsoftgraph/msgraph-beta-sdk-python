from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_instance_decision_item_access_package_assignment_policy_resource, access_review_instance_decision_item_azure_role_resource, access_review_instance_decision_item_service_principal_resource

class AccessReviewInstanceDecisionItemResource(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewInstanceDecisionItemResource and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Display name of the resource
        self._display_name: Optional[str] = None
        # Resource ID
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Type of resource. Types include: Group, ServicePrincipal, DirectoryRole, AzureRole, AccessPackageAssignmentPolicy.
        self._type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.accessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource":
                from . import access_review_instance_decision_item_access_package_assignment_policy_resource

                return access_review_instance_decision_item_access_package_assignment_policy_resource.AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource()
            if mapping_value == "#microsoft.graph.accessReviewInstanceDecisionItemAzureRoleResource":
                from . import access_review_instance_decision_item_azure_role_resource

                return access_review_instance_decision_item_azure_role_resource.AccessReviewInstanceDecisionItemAzureRoleResource()
            if mapping_value == "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource":
                from . import access_review_instance_decision_item_service_principal_resource

                return access_review_instance_decision_item_service_principal_resource.AccessReviewInstanceDecisionItemServicePrincipalResource()
        return AccessReviewInstanceDecisionItemResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the resource
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the resource
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_instance_decision_item_access_package_assignment_policy_resource, access_review_instance_decision_item_azure_role_resource, access_review_instance_decision_item_service_principal_resource

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Resource ID
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Resource ID
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Type of resource. Types include: Group, ServicePrincipal, DirectoryRole, AzureRole, AccessPackageAssignmentPolicy.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Type of resource. Types include: Group, ServicePrincipal, DirectoryRole, AzureRole, AccessPackageAssignmentPolicy.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

