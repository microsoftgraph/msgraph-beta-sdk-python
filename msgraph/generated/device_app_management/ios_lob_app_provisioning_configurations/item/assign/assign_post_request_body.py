from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_lob_app_provisioning_configuration_assignment = lazy_import('msgraph.generated.models.ios_lob_app_provisioning_configuration_assignment')
mobile_app_provisioning_config_group_assignment = lazy_import('msgraph.generated.models.mobile_app_provisioning_config_group_assignment')

class AssignPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the assign method.
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
    def app_provisioning_configuration_group_assignments(self,) -> Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]]:
        """
        Gets the appProvisioningConfigurationGroupAssignments property value. The appProvisioningConfigurationGroupAssignments property
        Returns: Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]]
        """
        return self._app_provisioning_configuration_group_assignments
    
    @app_provisioning_configuration_group_assignments.setter
    def app_provisioning_configuration_group_assignments(self,value: Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]] = None) -> None:
        """
        Sets the appProvisioningConfigurationGroupAssignments property value. The appProvisioningConfigurationGroupAssignments property
        Args:
            value: Value to set for the appProvisioningConfigurationGroupAssignments property.
        """
        self._app_provisioning_configuration_group_assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The appProvisioningConfigurationGroupAssignments property
        self._app_provisioning_configuration_group_assignments: Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]] = None
        # The iOSLobAppProvisioningConfigAssignments property
        self._i_o_s_lob_app_provisioning_config_assignments: Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_provisioning_configuration_group_assignments": lambda n : setattr(self, 'app_provisioning_configuration_group_assignments', n.get_collection_of_object_values(mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment)),
            "i_o_s_lob_app_provisioning_config_assignments": lambda n : setattr(self, 'i_o_s_lob_app_provisioning_config_assignments', n.get_collection_of_object_values(ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment)),
        }
        return fields
    
    @property
    def i_o_s_lob_app_provisioning_config_assignments(self,) -> Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]]:
        """
        Gets the iOSLobAppProvisioningConfigAssignments property value. The iOSLobAppProvisioningConfigAssignments property
        Returns: Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]]
        """
        return self._i_o_s_lob_app_provisioning_config_assignments
    
    @i_o_s_lob_app_provisioning_config_assignments.setter
    def i_o_s_lob_app_provisioning_config_assignments(self,value: Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]] = None) -> None:
        """
        Sets the iOSLobAppProvisioningConfigAssignments property value. The iOSLobAppProvisioningConfigAssignments property
        Args:
            value: Value to set for the iOSLobAppProvisioningConfigAssignments property.
        """
        self._i_o_s_lob_app_provisioning_config_assignments = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("appProvisioningConfigurationGroupAssignments", self.app_provisioning_configuration_group_assignments)
        writer.write_collection_of_object_values("iOSLobAppProvisioningConfigAssignments", self.i_o_s_lob_app_provisioning_config_assignments)
        writer.write_additional_data_value(self.additional_data)
    

