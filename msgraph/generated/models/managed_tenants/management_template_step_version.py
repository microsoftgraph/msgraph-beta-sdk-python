from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
management_template_step = lazy_import('msgraph.generated.models.managed_tenants.management_template_step')
management_template_step_deployment = lazy_import('msgraph.generated.models.managed_tenants.management_template_step_deployment')

class ManagementTemplateStepVersion(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def accepted_for(self,) -> Optional[management_template_step.ManagementTemplateStep]:
        """
        Gets the acceptedFor property value. The acceptedFor property
        Returns: Optional[management_template_step.ManagementTemplateStep]
        """
        return self._accepted_for
    
    @accepted_for.setter
    def accepted_for(self,value: Optional[management_template_step.ManagementTemplateStep] = None) -> None:
        """
        Sets the acceptedFor property value. The acceptedFor property
        Args:
            value: Value to set for the acceptedFor property.
        """
        self._accepted_for = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managementTemplateStepVersion and sets the default values.
        """
        super().__init__()
        # The acceptedFor property
        self._accepted_for: Optional[management_template_step.ManagementTemplateStep] = None
        # The contentMarkdown property
        self._content_markdown: Optional[str] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The deployments property
        self._deployments: Optional[List[management_template_step_deployment.ManagementTemplateStepDeployment]] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The templateStep property
        self._template_step: Optional[management_template_step.ManagementTemplateStep] = None
        # The version property
        self._version: Optional[int] = None
        # The versionInformation property
        self._version_information: Optional[str] = None
    
    @property
    def content_markdown(self,) -> Optional[str]:
        """
        Gets the contentMarkdown property value. The contentMarkdown property
        Returns: Optional[str]
        """
        return self._content_markdown
    
    @content_markdown.setter
    def content_markdown(self,value: Optional[str] = None) -> None:
        """
        Sets the contentMarkdown property value. The contentMarkdown property
        Args:
            value: Value to set for the contentMarkdown property.
        """
        self._content_markdown = value
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The createdByUserId property
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The createdByUserId property
        Args:
            value: Value to set for the createdByUserId property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateStepVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStepVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementTemplateStepVersion()
    
    @property
    def deployments(self,) -> Optional[List[management_template_step_deployment.ManagementTemplateStepDeployment]]:
        """
        Gets the deployments property value. The deployments property
        Returns: Optional[List[management_template_step_deployment.ManagementTemplateStepDeployment]]
        """
        return self._deployments
    
    @deployments.setter
    def deployments(self,value: Optional[List[management_template_step_deployment.ManagementTemplateStepDeployment]] = None) -> None:
        """
        Sets the deployments property value. The deployments property
        Args:
            value: Value to set for the deployments property.
        """
        self._deployments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accepted_for": lambda n : setattr(self, 'accepted_for', n.get_object_value(management_template_step.ManagementTemplateStep)),
            "content_markdown": lambda n : setattr(self, 'content_markdown', n.get_str_value()),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployments": lambda n : setattr(self, 'deployments', n.get_collection_of_object_values(management_template_step_deployment.ManagementTemplateStepDeployment)),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "template_step": lambda n : setattr(self, 'template_step', n.get_object_value(management_template_step.ManagementTemplateStep)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "version_information": lambda n : setattr(self, 'version_information', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The lastActionByUserId property
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The lastActionByUserId property
        Args:
            value: Value to set for the lastActionByUserId property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The lastActionDateTime property
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The lastActionDateTime property
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("acceptedFor", self.accepted_for)
        writer.write_str_value("contentMarkdown", self.content_markdown)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("deployments", self.deployments)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("templateStep", self.template_step)
        writer.write_int_value("version", self.version)
        writer.write_str_value("versionInformation", self.version_information)
    
    @property
    def template_step(self,) -> Optional[management_template_step.ManagementTemplateStep]:
        """
        Gets the templateStep property value. The templateStep property
        Returns: Optional[management_template_step.ManagementTemplateStep]
        """
        return self._template_step
    
    @template_step.setter
    def template_step(self,value: Optional[management_template_step.ManagementTemplateStep] = None) -> None:
        """
        Sets the templateStep property value. The templateStep property
        Args:
            value: Value to set for the templateStep property.
        """
        self._template_step = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. The version property
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. The version property
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    
    @property
    def version_information(self,) -> Optional[str]:
        """
        Gets the versionInformation property value. The versionInformation property
        Returns: Optional[str]
        """
        return self._version_information
    
    @version_information.setter
    def version_information(self,value: Optional[str] = None) -> None:
        """
        Sets the versionInformation property value. The versionInformation property
        Args:
            value: Value to set for the versionInformation property.
        """
        self._version_information = value
    

